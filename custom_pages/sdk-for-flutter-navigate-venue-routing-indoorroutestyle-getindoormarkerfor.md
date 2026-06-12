---
title: "getIndoorMarkerFor abstract method"
slug: "sdk-for-flutter-navigate-venue-routing-indoorroutestyle-getindoormarkerfor"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- getIndoorMarkerFor.html -->


<div>
<h1>getIndoorMarkerFor abstract method</h1></div>

<a href="/sdk-for-flutter-navigate-mapview-mapmarker-class">MapMarker</a>?
getIndoorMarkerFor(<ol class="parameter-list single-line"> <li><a href="/sdk-for-flutter-navigate-routing-indoorlevelchangefeatures">IndoorLevelChangeFeatures</a> feature, </li>
<li>int deltaZ</li>
</ol>)

      

    

<p>Returns a <a href="/sdk-for-flutter-navigate-mapview-mapmarker-class">MapMarker</a> for a given indoor feature and
the number of levels to change.</p>
<p>By default, no map markers are provided.</p>
<ul>
<li>
<p><code>feature</code> An indoor feature.</p>
</li>
<li>
<p><code>deltaZ</code> A number of levels to change, positive for up, negative for down.
In the case of 0, the method returns an exit map marker.</p>
</li>
</ul>
<p>Returns <a href="/sdk-for-flutter-navigate-mapview-mapmarker-class">MapMarker?</a>. The result <a href="/sdk-for-flutter-navigate-mapview-mapmarker-class">MapMarker</a>, if it was set.</p>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">MapMarker? getIndoorMarkerFor(IndoorLevelChangeFeatures feature, int deltaZ);</code></pre>

 



</div>
`
}</HTMLBlock>
