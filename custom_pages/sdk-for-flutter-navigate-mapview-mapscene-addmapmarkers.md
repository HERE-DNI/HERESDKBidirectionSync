---
title: "addMapMarkers abstract method"
slug: "sdk-for-flutter-navigate-mapview-mapscene-addmapmarkers"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- addMapMarkers.html -->


<div>
<h1>addMapMarkers abstract method</h1></div>

void
addMapMarkers(<ol class="parameter-list single-line"> <li>List&lt;<a href="/sdk-for-flutter-navigate-mapview-mapmarker-class">MapMarker</a>&gt; markers</li>
</ol>)

      

    

<p>Adds multiple map markers to this map scene.</p>
<p>Adding the same marker instances multiple times
has no effect. Adding markers that are already part of a map marker cluster has no effect.</p>
<p><strong>Note:</strong>
Due to technical limitations using the MapMarkers API to add a very large number of markers
(several thousands, especially 10000+) is not recommended. Adding this many markers will have
a negative impact on the performance leading to stuttering of the app and lower frame rates.
To work around this limitation add only map items which are in the current camera viewport.
A guide on how to achieve this can be found towards the end of the <a href="/sdk-for-flutter-navigate-mapview-mapscene-class">MapScene</a> class doc.</p>
<ul>
<li><code>markers</code> The list of markers to be added to this map scene.</li>
</ul>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">void addMapMarkers(List&lt;MapMarker&gt; markers);</code></pre>

 



</div>
`
}</HTMLBlock>
