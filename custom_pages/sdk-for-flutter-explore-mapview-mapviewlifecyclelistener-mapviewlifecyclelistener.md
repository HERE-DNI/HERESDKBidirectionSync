---
title: "MapViewLifecycleListener constructor"
slug: "sdk-for-flutter-explore-mapview-mapviewlifecyclelistener-mapviewlifecyclelistener"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- MapViewLifecycleListener.html -->


<div>
<h1>MapViewLifecycleListener constructor</h1></div>

MapViewLifecycleListener(<ol class="parameter-list"> <li>void onAttachLambda(<ol class="parameter-list single-line"> <li><a href="sdk-for-flutter-explore-mapview-mapviewbase-class">MapViewBase</a></li>
</ol>), </li>
<li>void onDetachLambda(<ol class="parameter-list single-line"> <li><a href="sdk-for-flutter-explore-mapview-mapviewbase-class">MapViewBase</a></li>
</ol>), </li>
<li>void onPauseLambda(), </li>
<li>void onResumeLambda(), </li>
<li>void onDestroyLambda(), </li>
</ol>)
    

<p>Provides a mechanism for observing a lifecycle of a map view and/or implementing components
whose lifecycle needs to be linked with that of a map view.</p>
<p>A <code>MapView</code> is using a</p>
<p><a href="https://developer.android.com/reference/android/view/SurfaceView">SurfaceView</a> for Android and
<a href="https://developer.apple.com/documentation/quartzcore/cametallayer">CAMetalLayer</a> for iOS
to render its content.</p>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">factory MapViewLifecycleListener(
  void Function(MapViewBase) onAttachLambda,
  void Function(MapViewBase) onDetachLambda,
  void Function() onPauseLambda,
  void Function() onResumeLambda,
  void Function() onDestroyLambda,

) =&gt; MapViewLifecycleListener$Lambdas(
  onAttachLambda,
  onDetachLambda,
  onPauseLambda,
  onResumeLambda,
  onDestroyLambda,

);</code></pre>

 



</div>
`
}</HTMLBlock>
