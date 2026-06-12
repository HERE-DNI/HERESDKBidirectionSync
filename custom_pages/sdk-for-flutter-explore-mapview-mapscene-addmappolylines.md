---
title: "addMapPolylines abstract method"
slug: "sdk-for-flutter-explore-mapview-mapscene-addmappolylines"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- addMapPolylines.html -->


<div>
<h1>addMapPolylines abstract method</h1></div>

void
addMapPolylines(<ol class="parameter-list single-line"> <li>List&lt;<a href="/sdk-for-flutter-explore-mapview-mappolyline-class">MapPolyline</a>&gt; mapPolylines</li>
</ol>)

      

    

<p>Adds map polylines to this map scene.</p>
<p><strong>Note:</strong>
Due to technical limitations using the MapPolyline API to add a very large number of
polylines (especially 1000+ also depending on their complexity) is not recommended.
Adding this many polylines has a negative impact on the performance leading to
stuttering of the app and lower frame rates.
To work around this limitation add only map items which are in the current camera viewport.
A guide on how to achieve this can be found towards the end of the <a href="/sdk-for-flutter-explore-mapview-mapscene-class">MapScene</a> class doc.</p>
<ul>
<li><code>mapPolylines</code> The map polylines to be added to this map scene.</li>
</ul>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">void addMapPolylines(List&lt;MapPolyline&gt; mapPolylines);</code></pre>

 



</div>
`
}</HTMLBlock>
