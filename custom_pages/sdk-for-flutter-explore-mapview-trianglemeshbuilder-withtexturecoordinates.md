---
title: "withTextureCoordinates abstract method"
slug: "sdk-for-flutter-explore-mapview-trianglemeshbuilder-withtexturecoordinates"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- withTextureCoordinates.html -->


<div>
<h1>withTextureCoordinates abstract method</h1></div>

<a href="/sdk-for-flutter-explore-mapview-meshbuilder-class">MeshBuilder</a>
withTextureCoordinates(<ol class="parameter-list single-line"> <li><a href="/sdk-for-flutter-explore-core-anchor2d-class">Anchor2D</a> a, </li>
<li><a href="/sdk-for-flutter-explore-core-anchor2d-class">Anchor2D</a> b, </li>
<li><a href="/sdk-for-flutter-explore-core-anchor2d-class">Anchor2D</a> c</li>
</ol>)

      

    

<p>Adds texture coordinates to a triangle.</p>
<p>Coordinates are specified as <code>&lt;u,v&gt;</code> with <code>&lt;0,0&gt;</code>
representing the bottom-left and <code>&lt;1,1&gt;</code> upper-right corner.</p>
<ul>
<li>
<p><code>a</code> Texture coordinate for vertex a. See <a href="/sdk-for-flutter-explore-mapview-meshbuilder-triangle">MeshBuilder.triangle</a></p>
</li>
<li>
<p><code>b</code> Texture coordinate for vertex b. See <a href="/sdk-for-flutter-explore-mapview-meshbuilder-triangle">MeshBuilder.triangle</a></p>
</li>
<li>
<p><code>c</code> Texture coordinate for vertex c. See <a href="/sdk-for-flutter-explore-mapview-meshbuilder-triangle">MeshBuilder.triangle</a></p>
</li>
</ul>
<p>Returns <a href="/sdk-for-flutter-explore-mapview-meshbuilder-class">MeshBuilder</a>. A <a href="/sdk-for-flutter-explore-mapview-meshbuilder-class">MeshBuilder</a> instance.</p>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">MeshBuilder withTextureCoordinates(Anchor2D a, Anchor2D b, Anchor2D c);</code></pre>

 



</div>
`
}</HTMLBlock>
