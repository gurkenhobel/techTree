using UnityEngine;
using System.Collections;
using Gurkenhobel.TechTree.Enums;

namespace Gurkenhobel.TechTree.Upgrades
{
    public class Reg1 : IUpgrade
    {
        public UpgradeLayer Layer { get; set; }

        public CharacterStats Apply(CharacterStats stats)
        {
            stats.HealthPoints -= 5;
            stats.HealthRegenPerSecond += 1.0f;
            return stats;
        }

        public string Name { get; set; }
    }
}
