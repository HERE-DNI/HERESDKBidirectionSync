---
title: "MapViewLifecycleListener constructor"
slug: "sdk-for-flutter-navigate-mapview-mapviewlifecyclelistener-mapviewlifecyclelistener"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- MapViewLifecycleListener.html -->
<div class="doc-with-sidebar"><div class="doc-content">
<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li>/sdk-for-flutter-navigate</li>
<li>/sdk-for-flutter-navigate-mapview-mapview-library</li>
<li>/sdk-for-flutter-navigate-mapview-mapviewlifecyclelistener-class</li>
<li class="self-crumb">MapViewLifecycleListener factory constructor</li>
</ol>
<div class="self-name">MapViewLifecycleListener</div>
<form class="search navbar-right" role="search">
<input autocomplete="off" class="form-control typeahead" disabled="" id="search-box" placeholder="Loading search..." type="text"/>
</form>
<div class="toggle" id="theme-button" title="Toggle brightness">
<label for="theme">
<input id="theme" type="checkbox" value="light-theme"/>

        dark_mode
      

        light_mode
      
</label>
</div>
</header>
<main>
<div class="main-content" data-above-sidebar="mapview/MapViewLifecycleListener-class-sidebar.html" data-below-sidebar="" id="dartdoc-main-content">
<div>
<h1>MapViewLifecycleListener constructor</h1></div>
<section class="multi-line-signature">
MapViewLifecycleListener(<wbr/><ol class="parameter-list"> <li>void onAttachLambda(<ol class="parameter-list single-line"> <li>/sdk-for-flutter-navigate-mapview-mapviewbase-class</li>
</ol>), </li>
<li>void onDetachLambda(<ol class="parameter-list single-line"> <li>/sdk-for-flutter-navigate-mapview-mapviewbase-class</li>
</ol>), </li>
<li>void onPauseLambda(), </li>
<li>void onResumeLambda(), </li>
<li>void onDestroyLambda(), </li>
</ol>)
    </section>
<section class="desc markdown">
<p>Provides a mechanism for observing a lifecycle of a map view and/or implementing components
whose lifecycle needs to be linked with that of a map view.</p>
<p>A <code>MapView</code> is using a</p>
<p><a href="https://developer.android.com/reference/android/view/SurfaceView">SurfaceView</a> for Android and
<a href="https://developer.apple.com/documentation/quartzcore/cametallayer">CAMetalLayer</a> for iOS
to render its content.</p>
</section>
<section class="summary source-code" id="source">
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
</section>
</div>
<div class="sidebar sidebar-offcanvas-left" id="dartdoc-sidebar-left">
<header class="hidden-l" id="header-search-sidebar">
<form class="search-sidebar" role="search">
<input autocomplete="off" class="form-control typeahead" disabled="" id="search-sidebar" placeholder="Loading search..." type="text"/>
</form>
</header>
<ol class="breadcrumbs gt-separated dark hidden-l" id="sidebar-nav">
<li>/sdk-for-flutter-navigate</li>
<li>/sdk-for-flutter-navigate-mapview-mapview-library</li>
<li>/sdk-for-flutter-navigate-mapview-mapviewlifecyclelistener-class</li>
<li class="self-crumb">MapViewLifecycleListener factory constructor</li>
</ol>
<h5>MapViewLifecycleListener class</h5>
<div id="dartdoc-sidebar-left-content"></div>
</div>
<div class="sidebar sidebar-offcanvas-right" id="dartdoc-sidebar-right">
</div>
</main>
<footer>

    here_sdk
      4.26.0
  
</footer>
</div></div>
</div>
`
}</HTMLBlock>
