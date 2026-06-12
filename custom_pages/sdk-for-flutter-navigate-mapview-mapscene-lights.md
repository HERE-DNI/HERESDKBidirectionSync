---
title: "lights property"
slug: "sdk-for-flutter-navigate-mapview-mapscene-lights"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- lights.html -->


<div>
<h1>lights property</h1></div>
<section id="getter">

<a href="/sdk-for-flutter-navigate-mapview-mapscenelights-class">MapSceneLights</a>
lights


<p>Controls lights present in the scene.
Provides access to a MapSceneLights instance that controls the lights in the scene.</p>
<p>The behavior of the returned MapSceneLights instance depends on the state of the scene:</p>
<ul>
<li>If the scene is not loaded, the returned MapSceneLights instance will not contain any light settings, as lights are not loaded without a scene.</li>
<li>If the scene is loaded, the returned MapSceneLights instance reflects the current light settings of the loaded scene.</li>
</ul>
<p>Scene Change Behavior:</p>
<ul>
<li>If the scene changes, the MapSceneLights instance will be updated to reflect the light settings of the new scene.</li>
<li>Any user-defined settings to MapSceneLights will be overridden by the new scene's light settings when the scene changes.</li>
</ul>
<p>Error Handling:</p>
<ul>
<li>If the scene is loaded and the loaded scene does not utilize or specify light settings:
<ul>
<li>If the lights are not present, the error callback may return a NO_LIGHTS state.
Gets a MapSceneLights instance that controls lights present in the scene.</li>
</ul>
</li>
</ul>
<p>Note: This is a beta release of this feature, so there could be a few bugs and unexpected behaviors.
Related APIs may change for new releases without a deprecation process.</p>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">MapSceneLights get lights;</code></pre>

</section>
 



</div>
`
}</HTMLBlock>
