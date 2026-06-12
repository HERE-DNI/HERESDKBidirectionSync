---
title: "MeshBuilder class abstract"
slug: "sdk-for-flutter-navigate-mapview-meshbuilder-class"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- MeshBuilder-class.html -->


<div>
<h1>MeshBuilder class abstract</h1></div>

<p>Builder for meshes.</p>
<p>Such meshes can contain different kinds of primitives, like quads or
triangles. Both primitives support adding texture coordinates that are mapped to the
corners of the primitives. See <a href="/sdk-for-flutter-navigate-mapview-trianglemeshbuilder-class">TriangleMeshBuilder</a> and <a href="/sdk-for-flutter-navigate-mapview-quadmeshbuilder-class">QuadMeshBuilder</a> for more details.</p>
<p>Note: Normals cannot be set as they are not necessary when using the <a href="/sdk-for-flutter-navigate-mapview-meshbuilder-class">MeshBuilder</a>.</p>
<p>Example how to build a cube using <a href="/sdk-for-flutter-navigate-mapview-quadmeshbuilder-class">QuadMeshBuilder</a></p>
<pre class="language-dart"><code>Mesh? cube = MeshBuilder()
      .quad(Point3D(0.5, 0.5, 0.5),
            Point3D(-0.5, 0.5, 0.5),
            Point3D(0.5, -0.5, 0.5),
            Point3D(-0.5, -0.5, 0.5))
      .quad(Point3D(-0.5, 0.5, -0.5),
            Point3D(0.5, 0.5, -0.5),
            Point3D(-0.5, -0.5, -0.5),
            Point3D(0.5, -0.5, -0.5))
      .quad(Point3D(0.5, 0.5, -0.5),
            Point3D(0.5, 0.5, 0.5),
            Point3D(0.5, -0.5, -0.5),
            Point3D(0.5, -0.5, 0.5))
      .quad(Point3D(-0.5, 0.5, 0.5),
            Point3D(-0.5, 0.5, -0.5),
            Point3D(-0.5, -0.5, 0.5),
            Point3D(-0.5, -0.5, -0.5))
      .quad(Point3D(-0.5, 0.5, 0.5),
            Point3D(0.5, 0.5, 0.5),
            Point3D(-0.5, 0.5, -0.5),
            Point3D(0.5, 0.5, -0.5))
      .quad(Point3D(0.5, -0.5, 0.5),
            Point3D(-0.5, -0.5, 0.5),
            Point3D(0.5, -0.5, -0.5),
            Point3D(-0.5, -0.5, -0.5))
      .build();
</code></pre>


<ul><li>Implementers</li></ul>


<h2>Constructors</h2>
<ul><li><a href="/sdk-for-flutter-navigate-mapview-meshbuilder-meshbuilder">MeshBuilder</a></li></ul>


<h2>Properties</h2>
<ul><li><a href="/sdk-for-flutter-navigate-mapview-meshbuilder-hashcode">hashCode</a></li><li><a href="/sdk-for-flutter-navigate-mapview-meshbuilder-runtimetype">runtimeType</a></li></ul>


<h2>Methods</h2>
<ul><li><a href="/sdk-for-flutter-navigate-mapview-meshbuilder-build">build</a></li><li><a href="/sdk-for-flutter-navigate-mapview-meshbuilder-nosuchmethod">noSuchMethod</a></li><li><a href="/sdk-for-flutter-navigate-mapview-meshbuilder-quad">quad</a></li><li><a href="/sdk-for-flutter-navigate-mapview-meshbuilder-tostring">toString</a></li><li><a href="/sdk-for-flutter-navigate-mapview-meshbuilder-triangle">triangle</a></li></ul>


<h2>Operators</h2>
<ul><li><a href="/sdk-for-flutter-navigate-mapview-meshbuilder-operator-equals">operator ==</a></li></ul>

 



</div>
`
}</HTMLBlock>
