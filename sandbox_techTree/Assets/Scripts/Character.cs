using UnityEngine;
using System.Collections;
using Gurkenhobel.TechTree.Components;

namespace Gurkenhobel.TechTree
{


    [RequireComponent(typeof(AudioSource))]
    public class Character : MonoBehaviour
    {

        private CharacterStats _characterStats;
        private AudioSource _audioSource1;
        private AudioSource _audioSource2;
        public Animator Animator;
        public HealthBar HealthBar;


        public readonly CharacterStats _baseStats = new CharacterStats()
        {
            AttackSpeed = 1,
            AttackStrength = 1,
            CritChance = 5,
            CritFactor = 2.0f,
            DefencePoints = 0.5f,
            HealthPoints = 10,
            MaxHealthPoints = 10,
            HealthRegenPerSecond = 0.1f
        };

        public CharacterStats CharacterStats
        {
            get { return _characterStats; }
            set { _characterStats = value; }
        }

        public void GetAttacked()
        {
            Animator.Play("damage1");
            _audioSource1.PlayDelayed(0.2f);
        }

        public void Attack()
        {
            Animator.Play("attack1");
            _audioSource2.Play();
        }

        private void Awake()
        {
            CharacterStats = _baseStats.Clone();
            _audioSource1 = GetComponents<AudioSource>()[0];
            _audioSource2 = GetComponents<AudioSource>()[1];
        }

        private void Update()
        {
            HealthBar.MaxValue = CharacterStats.MaxHealthPoints;
            HealthBar.CurrentValue = CharacterStats.HealthPoints;
        }

    }
}
