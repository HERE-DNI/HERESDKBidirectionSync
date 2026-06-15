---
title: "loadScene abstract method"
slug: "sdk-for-flutter-explore-mapview-mapscene-loadscene"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- loadScene.html -->


<div>
<h1>loadScene abstract method</h1></div>

void
loadScene(<ol class="parameter-list single-line"> <li><a href="sdk-for-flutter-explore-mapview-mapsceneloadoptions-class">MapSceneLoadOptions</a> options, </li>
<li><a href="sdk-for-flutter-explore-mapview-mapsceneloadscenecallback">MapSceneLoadSceneCallback</a>? callback</li>
</ol>)

      

    

<p>Asynchronously loads a map scene using MapSceneLoadOptions.</p>
<p>This is an unified API that supports loading from either a map scheme or configuration file,
with optional feature and watermark configuration. It's more efficient to load the scene with
this function by specifying the list of enabled features and disabled features, compared to
loading the scene first and enabling or disabling map features in the scene loading callback
function.</p>
<p>Configuration defaults are used for features that are not part of the enabled features or
disabled features parameters. When a feature is in both the enabled and disabled lists,
the feature is considered as requested to be enabled. If the same feature is present multiple
times in the enabled list with different modes, then the feature is considered as requested
to be enabled, but with an unspecified mode (any of the many specified in the enabled list).</p>
<p>Any previous map scene config will be replaced. The callback is called on the main thread.</p>
<p>Note: This is a beta release of this feature, so there could be a few bugs and unexpected behaviors.
Related APIs may change for new releases without a deprecation process.</p>
<ul>
<li>
<p><code>options</code> Scene configuration options created using MapSceneLoadOptionsBuilder.</p>
</li>
<li>
<p><code>callback</code> Optional callback that will receive the result of this operation.</p>
</li>
</ul>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">void loadScene(MapSceneLoadOptions options, MapSceneLoadSceneCallback? callback);</code></pre>

 



</div>
`
}</HTMLBlock>
