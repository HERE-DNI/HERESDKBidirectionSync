---
title: "MapSceneLightsAttributeSettingCallback typedef"
slug: "sdk-for-flutter-explore-mapview-mapscenelightsattributesettingcallback"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- MapSceneLightsAttributeSettingCallback.html -->


<div>
<h1>MapSceneLightsAttributeSettingCallback typedef</h1></div>

MapSceneLightsAttributeSettingCallback =
     void Function(<a href="sdk-for-flutter-explore-mapview-mapscenelightsattributesettingerror">MapSceneLightsAttributeSettingError</a>? setLightError)


<p>This callback function allows handling errors that occur during the setting of light attributes.</p>
<ul>
<li><code>setLightError</code> The cause for the failure when setting the light attributes, or <code>null</code> if no error occurred.</li>
</ul>
<p>Note: The error code <code>NO_LIGHTS</code> may be returned when attempting to set light attributes in map schemes
that do not support lights, for instance <code>road.network</code> map scheme.</p>
<p>Please refer to the error code documentation for further details on error handling.</p>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">typedef MapSceneLightsAttributeSettingCallback = void Function(MapSceneLightsAttributeSettingError? setLightError);</code></pre>

 



</div>
`
}</HTMLBlock>
