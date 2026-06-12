---
title: "GeoPolygon constructor"
slug: "sdk-for-flutter-navigate-core-geopolygon-geopolygon"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- GeoPolygon.html -->


<div>
<h1>GeoPolygon constructor</h1></div>

GeoPolygon(<ol class="parameter-list single-line"> <li>List&lt;<a href="/sdk-for-flutter-navigate-core-geocoordinates-class">GeoCoordinates</a>&gt; vertices</li>
</ol>)
    

<p>Constructs an instance of this class from the provided vertices.</p>
<p>Throws InstantiationError if the number of vertices is less than three.</p>
<ul>
<li><code>vertices</code> List of vertices representing the polygon outer boundary in clockwise order.</li>
</ul>
<p>Throws <a href="/sdk-for-flutter-navigate-core-errors-instantiationexception-class">InstantiationException</a>. Instantiation error.</p>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">factory GeoPolygon(List&lt;GeoCoordinates&gt; vertices) =&gt; $prototype.$init(vertices);</code></pre>

 



</div>
`
}</HTMLBlock>
