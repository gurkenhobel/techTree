using UnityEngine;
using System.Collections;

namespace Gurkenhobel.TechTree
{



    public class GameController : MonoBehaviour
    {
        public PlayerChar playerCharacter;
        public GameObject enemyPrefab;
        public GameObject enemySpawn;
        public AnimationCurve EnemyStrengthCurve;
        public Scoreboard Scoreboard;

        private Character _enemyCharacter;
        private Components.TechTree _playerTechTree;
        private float _enemyAttackTimestamp = -1;
        private float _playerAttackTimestamp = -1;
        private float _healTimestamp = -1;
        private float _enemySpawnTimeStamp;

        private void SetEnemy(Character enemy)
        {
            _enemyCharacter = enemy;
            StartFight();
        }

        private void StartFight()
        {
            playerCharacter.CharacterStats.HealthPoints = playerCharacter.CharacterStats.MaxHealthPoints;
            _enemyAttackTimestamp = Time.time + _enemyCharacter.CharacterStats.AttackSpeed;
            _playerAttackTimestamp = Time.time + playerCharacter.CharacterStats.AttackSpeed;
            _healTimestamp = Time.time;
        }

        private void Attack(Character attacker, Character defender)
        {
            var dmg = attacker.CharacterStats.AttackStrength;
            if (IsCrit(attacker.CharacterStats.CritChance))
            {
                //Debug.Log("Crit!");
                dmg *= attacker.CharacterStats.CritFactor;
            }
            dmg -= defender.CharacterStats.DefencePoints;
            defender.CharacterStats.HealthPoints -= dmg;
        }

        private bool IsCrit(float critChance)
        {
            return Random.Range(1, 100) < critChance;
        }

        private CharacterStats GetEnemyStats()
        {
            var newStats = _enemyCharacter._baseStats.Clone();
            newStats.HealthPoints += EnemyStrengthCurve.Evaluate(Time.time - _enemySpawnTimeStamp) * 1 /*factor*/;
            newStats.AttackSpeed -= EnemyStrengthCurve.Evaluate(Time.time - _enemySpawnTimeStamp) * 0.5f /*factor*/;
            newStats.AttackStrength += EnemyStrengthCurve.Evaluate(Time.time - _enemySpawnTimeStamp) * 1 /*factor*/;
            newStats.CritChance += EnemyStrengthCurve.Evaluate(Time.time - _enemySpawnTimeStamp) * 1 /*factor*/;
            newStats.CritFactor += EnemyStrengthCurve.Evaluate(Time.time - _enemySpawnTimeStamp) * 1 /*factor*/;
            newStats.DefencePoints += EnemyStrengthCurve.Evaluate(Time.time - _enemySpawnTimeStamp) * 1 /*factor*/;
            newStats.HealthRegenPerSecond += EnemyStrengthCurve.Evaluate(Time.time - _enemySpawnTimeStamp) * 0.1f /*factor*/;
            newStats.MaxHealthPoints = newStats.HealthPoints;
            return newStats;
        }

        private void SpawnEnemy()
        {
            var testEnemyGo = Instantiate(enemyPrefab);
            testEnemyGo.transform.position = enemySpawn.transform.position;
            SetEnemy(testEnemyGo.GetComponent<Character>());

            _enemyCharacter.CharacterStats = GetEnemyStats();
            //Debug.Log("new enemy spawned");
            Scoreboard.Level++;
        }

        // Use this for initialization
        void Start()
        {
            _playerTechTree = GetComponent<Components.TechTree>();
            playerCharacter.UpgradesChanged(_playerTechTree.GetUpgrades());
            _enemySpawnTimeStamp = Time.time;
            SpawnEnemy();
        }

        private void RecalculateGameState()
        {
            if (_playerAttackTimestamp != -1)
            {
                //PlayerAttack
                if (Time.time >= _playerAttackTimestamp)
                {
                    Attack(playerCharacter, _enemyCharacter);
                    playerCharacter.Attack();
                    _enemyCharacter.GetAttacked();
                    _playerAttackTimestamp = Time.time + playerCharacter.CharacterStats.AttackSpeed;
                    //Debug.Log("player hp: " + playerCharacter.CharacterStats.HealthPoints);
                }

                //EnemyAttack
                if (Time.time >= _enemyAttackTimestamp)
                {
                    Attack(_enemyCharacter, playerCharacter);
                    _enemyCharacter.Attack();
                    playerCharacter.GetAttacked();
                    _enemyAttackTimestamp = Time.time + _enemyCharacter.CharacterStats.AttackSpeed;
                    //Debug.Log("enemy hp: " + _enemyCharacter.CharacterStats.HealthPoints);
                }

                //PlayerDeath
                if (playerCharacter.CharacterStats.HealthPoints < 0)
                {
                    _playerAttackTimestamp = -1;
                    Destroy(playerCharacter.gameObject);
                    Debug.Log("player died");
                }

                //EnemyDeath
                if (_enemyCharacter.CharacterStats.HealthPoints < 0)
                {
                    Destroy(_enemyCharacter.gameObject);
                    Debug.Log("enemy died");
                    if (_playerAttackTimestamp != -1)
                    {
                        //SpawnNextEnemy
                        SpawnEnemy();
                    }
                }

                if (Time.time >= _healTimestamp)
                {
                    _healTimestamp = Time.time + 0.1f;
                    //PlayerRegen
                    playerCharacter.CharacterStats.HealthPoints =
                        Mathf.Clamp(playerCharacter.CharacterStats.HealthRegenPerSecond / 10 +
                                    playerCharacter.CharacterStats.HealthPoints, 0,
                            playerCharacter.CharacterStats.MaxHealthPoints);

                    //EnemyRegen
                    _enemyCharacter.CharacterStats.HealthPoints =
                        Mathf.Clamp(_enemyCharacter.CharacterStats.HealthRegenPerSecond / 10 +
                                    _enemyCharacter.CharacterStats.HealthPoints, 0,
                            _enemyCharacter.CharacterStats.MaxHealthPoints);
                }
            }
        }


        // Update is called once per frame
        void Update()
        {
            RecalculateGameState();
            if (Input.GetKeyDown(KeyCode.Space))
            {
                Time.timeScale = 0;
            }
            if (Input.GetKeyUp(KeyCode.Space))
            {
                Time.timeScale = 1;
            }
        }
    }
}
