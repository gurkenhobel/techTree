using UnityEngine;
using System.Collections;
using Gurkenhobel.TechTree;
using Gurkenhobel.TechTree.Enums;

public class AtkSpd0_5 : IUpgrade
{
    public UpgradeLayer Layer { get; set; }
    public CharacterStats Apply(CharacterStats stats)
    {
        stats.AttackSpeed -= 0.25f;
        stats.AttackStrength -= 0.1f;
        return stats;
    }

    public string Name { get; set; }
}
