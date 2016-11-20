using UnityEngine;
using System.Collections;
using System.Collections.Generic;

public class Node : MonoBehaviour
{

    public List<Node> Children;
    public GameObject ChildOf;

    private List<GameObject> _lines = new List<GameObject>();

    private void Awake()
    {

    }

    // Use this for initialization
    void Start()
    {
        if (Children == null) return;
        foreach (var c in Children)
        {
            var line = (GameObject)Instantiate(ChildOf, transform.position, transform.rotation);
            line.gameObject.transform.SetParent(gameObject.transform);
            _lines.Add(line);
            line.GetComponent<RectTransform>().Rotate(line.transform.forward, Vector3.Angle(line.transform.right, c.transform.position - transform.position));
        }
    }

    // Update is called once per frame
    void Update()
    {

    }
}
