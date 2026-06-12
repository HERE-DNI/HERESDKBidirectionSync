---
title: "addMapArrow abstract method"
slug: "sdk-for-flutter-navigate-mapview-mapscene-addmaparrow"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- addMapArrow.html -->


<div>
<h1>addMapArrow abstract method</h1></div>

void
addMapArrow(<ol class="parameter-list single-line"> <li><a href="/sdk-for-flutter-navigate-mapview-maparrow-class">MapArrow</a> mapArrow</li>
</ol>)

      

    

<p>Adds a map arrow to this map scene.</p>
<p><strong>Note:</strong>
Due to technical limitations using the MapArrow API to add a very large number of arrows
(especially 1000+ also depending on their complexity) is not recommended.
Adding this many arrows has a negative impact on the performance leading to stuttering of the
app and lower frame rates.
To work around this limitation add only map items which are in the current camera viewport.
A guide on how to achieve this can be found towards the end of the <a href="/sdk-for-flutter-navigate-mapview-mapscene-class">MapScene</a> class doc.</p>
<ul>
<li><code>mapArrow</code> The map arrow to be added to this map scene.</li>
</ul>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">void addMapArrow(MapArrow mapArrow);</code></pre>

 



</div>
`
}</HTMLBlock>
