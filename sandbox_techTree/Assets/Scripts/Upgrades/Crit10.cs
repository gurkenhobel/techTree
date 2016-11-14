using UnityEngine;
using System.Collections;
using Gurkenhobel.TechTree;
using Gurkenhobel.TechTree.Enums;

namespace Gurkenhobel.TechTree.Upgrades
{
    public class Crit10 : IUpgrade
    {
        public UpgradeLayer Layer { get; set; }
        public CharacterStats Apply(CharacterStats stats)
        {
            stats.CritChance += 10;
            return stats;
        }

        public string Name { get; set; }
    }
}

