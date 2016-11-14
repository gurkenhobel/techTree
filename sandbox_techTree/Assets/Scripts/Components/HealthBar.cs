using UnityEngine;
using System.Collections;

namespace Gurkenhobel.TechTree.Components
{



    public class HealthBar : MonoBehaviour
    {
        public GameObject Foreground;

        public float MaxValue;
        public float CurrentValue;

        void Start()
        {

        }

        // Update is called once per frame
        void Update()
        {
            var width = CurrentValue / MaxValue;
            var rt = Foreground.GetComponent<RectTransform>();
            rt.sizeDelta = new Vector2(width, rt.sizeDelta.y);
        }
    }
}
