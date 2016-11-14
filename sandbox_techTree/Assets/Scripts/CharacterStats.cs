using UnityEngine;
using System.Collections;
using UnityEngine.Assertions.Comparers;

namespace Gurkenhobel.TechTree
{



    public class CharacterStats
    {
        public float AttackSpeed { get; set; }
        public float AttackStrength { get; set; }
        public float CritChance { get; set; }
        public float CritFactor { get; set; }
        public float DefencePoints { get; set; }
        public float HealthPoints { get; set; }
        public float MaxHealthPoints { get; set; }
        public float HealthRegenPerSecond { get; set; }

        public CharacterStats Clone()
        {
            var res = new CharacterStats
            {
                AttackSpeed = this.AttackSpeed,
                AttackStrength = this.AttackStrength,
                CritChance = this.CritChance,
                CritFactor = this.CritFactor,
                DefencePoints = this.DefencePoints,
                HealthPoints = this.HealthPoints,
                MaxHealthPoints = this.MaxHealthPoints,
                HealthRegenPerSecond = this.HealthRegenPerSecond
            };
            return res;
        }
    }
}
