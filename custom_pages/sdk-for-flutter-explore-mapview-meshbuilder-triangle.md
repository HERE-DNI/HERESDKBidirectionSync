---
title: "triangle abstract method"
slug: "sdk-for-flutter-explore-mapview-meshbuilder-triangle"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- triangle.html -->


<div>
<h1>triangle abstract method</h1></div>

<a href="sdk-for-flutter-explore-mapview-trianglemeshbuilder-class">TriangleMeshBuilder</a>
triangle(<ol class="parameter-list single-line"> <li><a href="sdk-for-flutter-explore-core-point3d-class">Point3D</a> a, </li>
<li><a href="sdk-for-flutter-explore-core-point3d-class">Point3D</a> b, </li>
<li><a href="sdk-for-flutter-explore-core-point3d-class">Point3D</a> c</li>
</ol>)

      

    

<p>Adds a triangle.</p>
<p>Triangle visibility is determined via back-face culling. Front-facing
triangles are expected to have counter-clockwise winding.</p>
<ul>
<li>
<p><code>a</code> First vertex of the triangle.</p>
</li>
<li>
<p><code>b</code> Second vertex of the triangle.</p>
</li>
<li>
<p><code>c</code> Third vertex of the triangle.</p>
</li>
</ul>
<p>Returns <a href="sdk-for-flutter-explore-mapview-trianglemeshbuilder-class">TriangleMeshBuilder</a>. A <a href="sdk-for-flutter-explore-mapview-trianglemeshbuilder-class">TriangleMeshBuilder</a> instance.</p>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">TriangleMeshBuilder triangle(Point3D a, Point3D b, Point3D c);</code></pre>

 



</div>
`
}</HTMLBlock>
