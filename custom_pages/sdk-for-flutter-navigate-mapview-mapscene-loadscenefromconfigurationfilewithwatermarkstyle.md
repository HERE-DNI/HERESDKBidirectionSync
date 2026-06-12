---
title: "loadSceneFromConfigurationFileWithWatermarkStyle abstract method"
slug: "sdk-for-flutter-navigate-mapview-mapscene-loadscenefromconfigurationfilewithwatermarkstyle"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- loadSceneFromConfigurationFileWithWatermarkStyle.html -->


<div>
<h1>loadSceneFromConfigurationFileWithWatermarkStyle abstract method</h1></div>

void
loadSceneFromConfigurationFileWithWatermarkStyle(<ol class="parameter-list single-line"> <li>String configurationFile, </li>
<li><a href="/sdk-for-flutter-navigate-mapview-watermarkstyle">WatermarkStyle</a> watermarkStyle, </li>
<li><a href="/sdk-for-flutter-navigate-mapview-mapsceneloadscenecallback">MapSceneLoadSceneCallback</a>? callback</li>
</ol>)

      

    

<p>Asynchronously loads a map scene described by a specified file in one of the supported formats.</p>
<p>The style of the HERE watermark matching the map scheme is specified. Any previous map scene
config will be replaced.</p>
<p>When loading the same file again, consider to call <code>reloadScene()</code> instead.</p>
<p>Map features enabled or disabled using <a href="/sdk-for-flutter-navigate-mapview-mapscene-enablefeatures">MapScene.enableFeatures</a>
and <a href="/sdk-for-flutter-navigate-mapview-mapscene-disablefeatures">MapScene.disableFeatures</a> will be reset to defaults for the new
scene configuration.</p>
<p>The callback is called on the main thread.</p>
<ul>
<li>
<p><code>configurationFile</code> Map scheme configuration file. It must contain the whole scene configuration.
In case it contains references to other files, they have to be reachable under
the paths specified in the main configuration file.</p>
</li>
<li>
<p><code>watermarkStyle</code> The style for the HERE watermark, see <a href="/sdk-for-flutter-navigate-mapview-watermarkstyle">WatermarkStyle</a>.</p>
</li>
<li>
<p><code>callback</code> Optional callback that will receive the result of this operation.</p>
</li>
</ul>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">void loadSceneFromConfigurationFileWithWatermarkStyle(String configurationFile, WatermarkStyle watermarkStyle, MapSceneLoadSceneCallback? callback);</code></pre>

 



</div>
`
}</HTMLBlock>
