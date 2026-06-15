---
title: "loadSceneForMapScheme abstract method"
slug: "sdk-for-flutter-navigate-mapview-mapscene-loadsceneformapscheme"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- loadSceneForMapScheme.html -->


<div>
<h1>loadSceneForMapScheme abstract method</h1></div>

void
loadSceneForMapScheme(<ol class="parameter-list single-line"> <li><a href="sdk-for-flutter-navigate-mapview-mapscheme">MapScheme</a> mapScheme, </li>
<li><a href="sdk-for-flutter-navigate-mapview-mapsceneloadscenecallback">MapSceneLoadSceneCallback</a>? callback</li>
</ol>)

      

    

<p>Asynchronously loads a map scene described by a specified map scheme.</p>
<p>Any previous map scene config will be replaced. The loaded scene is cached and so any changes
made to the scene files on disk might not get reflected on a successive call to this function.
Instead the reloadScene API can handle such use-cases to force-update the scene.</p>
<p>Map features enabled or disabled using <a href="sdk-for-flutter-navigate-mapview-mapscene-enablefeatures">MapScene.enableFeatures</a>
and <a href="sdk-for-flutter-navigate-mapview-mapscene-disablefeatures">MapScene.disableFeatures</a> will be reset to defaults for the new
scene configuration.</p>
<p>The callback is called on the main thread.</p>
<ul>
<li>
<p><code>mapScheme</code> Map scheme.</p>
</li>
<li>
<p><code>callback</code> Optional callback that will receive the result of this operation.</p>
</li>
</ul>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">void loadSceneForMapScheme(MapScheme mapScheme, MapSceneLoadSceneCallback? callback);</code></pre>

 



</div>
`
}</HTMLBlock>
