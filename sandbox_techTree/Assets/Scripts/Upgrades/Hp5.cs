using UnityEngine;
using System.Collections;
using Gurkenhobel.TechTree.Enums;

namespace Gurkenhobel.TechTree.Upgrades
{
    public class Hp5 : IUpgrade
    {
        public UpgradeLayer Layer { get; set; }

        public CharacterStats Apply(CharacterStats stats)
        {
            stats.HealthPoints += 5;
            stats.MaxHealthPoints += 5;
            return stats;
        }

        public string Name { get; set; }
    }
}
