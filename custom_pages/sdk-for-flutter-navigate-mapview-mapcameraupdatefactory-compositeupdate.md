---
title: "compositeUpdate static method"
slug: "sdk-for-flutter-navigate-mapview-mapcameraupdatefactory-compositeupdate"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- compositeUpdate.html -->


<div>
<h1>compositeUpdate static method</h1></div>

<a href="sdk-for-flutter-navigate-mapview-mapcameraupdate-class">MapCameraUpdate</a>
compositeUpdate(<ol class="parameter-list single-line"> <li>List&lt;<a href="sdk-for-flutter-navigate-mapview-mapcameraupdate-class">MapCameraUpdate</a>&gt; mapCameraUpdates</li>
</ol>)

      

    

<p>Creates a composite camera update from a list of camera updates.</p>
<p>The result update will be
equivalent to executing all given updates sequentially in the order they were provided.</p>
<p>MapCameraAnimation instances derived from the MapCameraAnimationFactory and a composite camera
update are not supported. An AnimationListener will receive an AnimationState.Cancelled signal
when trying to apply such animations.</p>
<ul>
<li><code>mapCameraUpdates</code> List of MapCamera updates.</li>
</ul>
<p>Returns <a href="sdk-for-flutter-navigate-mapview-mapcameraupdate-class">MapCameraUpdate</a>. MapCameraUpdate instance.</p>
<p>Throws <a href="sdk-for-flutter-navigate-mapview-mapcameraupdateinstantiationexception-class">MapCameraUpdateInstantiationException</a>. Indicates an instantiation issue.</p>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">static MapCameraUpdate compositeUpdate(List&lt;MapCameraUpdate&gt; mapCameraUpdates) =&gt; $prototype.compositeUpdate(mapCameraUpdates);</code></pre>

 



</div>
`
}</HTMLBlock>
