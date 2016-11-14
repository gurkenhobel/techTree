using System.Collections;
using Gurkenhobel.TechTree;
using Gurkenhobel.TechTree.Enums;
using JetBrains.Annotations;
using UnityEngine;

namespace Gurkenhobel.TechTree
{
    public interface IUpgrade
    {
        UpgradeLayer Layer { get; set; }

        CharacterStats Apply(CharacterStats stats);

        string Name { get; set; }
    }
}