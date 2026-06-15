---
title: "quad abstract method"
slug: "sdk-for-flutter-explore-mapview-meshbuilder-quad"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- quad.html -->


<div>
<h1>quad abstract method</h1></div>

<a href="sdk-for-flutter-explore-mapview-quadmeshbuilder-class">QuadMeshBuilder</a>
quad(<ol class="parameter-list"> <li><a href="sdk-for-flutter-explore-core-point3d-class">Point3D</a> a, </li>
<li><a href="sdk-for-flutter-explore-core-point3d-class">Point3D</a> b, </li>
<li><a href="sdk-for-flutter-explore-core-point3d-class">Point3D</a> c, </li>
<li><a href="sdk-for-flutter-explore-core-point3d-class">Point3D</a> d, </li>
</ol>)

      

    

<p>Adds a quad.</p>
<p>Internally, this will be transformed into triangles abc and bdc.</p>
<p>Triangle visibility is determined via back-face culling. Front-facing triangles are expected to have
counter-clockwise winding.</p>
<ul>
<li>
<p><code>a</code> First vertex of quad.</p>
</li>
<li>
<p><code>b</code> Second vertex of the quad.</p>
</li>
<li>
<p><code>c</code> Third vertex of the quad.</p>
</li>
<li>
<p><code>d</code> Fourth vertex of the quad.</p>
</li>
</ul>
<p>Returns <a href="sdk-for-flutter-explore-mapview-quadmeshbuilder-class">QuadMeshBuilder</a>. A <a href="sdk-for-flutter-explore-mapview-quadmeshbuilder-class">QuadMeshBuilder</a> instance.</p>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">QuadMeshBuilder quad(Point3D a, Point3D b, Point3D c, Point3D d);</code></pre>

 



</div>
`
}</HTMLBlock>
