---
title: "onPause abstract method"
slug: "sdk-for-flutter-navigate-maploader-mapupdateprogresslistener-onpause"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- onPause.html -->
<div class="doc-with-sidebar"><div class="doc-content">
<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li>/sdk-for-flutter-navigate</li>
<li>/sdk-for-flutter-navigate-maploader-maploader-library</li>
<li>/sdk-for-flutter-navigate-maploader-mapupdateprogresslistener-class</li>
<li class="self-crumb">onPause abstract method</li>
</ol>
<div class="self-name">onPause</div>
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
<div class="main-content" data-above-sidebar="maploader/MapUpdateProgressListener-class-sidebar.html" data-below-sidebar="" id="dartdoc-main-content">
<div>
<h1>onPause abstract method</h1></div>
<section class="multi-line-signature">
void
onPause(<wbr/><ol class="parameter-list single-line"> <li>/sdk-for-flutter-navigate-maploader-maploadererror? error</li>
</ol>)

      

    </section>
<section class="desc markdown">
<p>Called when update is paused.</p>
<p>Invoked on the main thread.</p>
<ul>
<li><code>error</code> Populated when a retryable error is the reason for a pause. A retryable error can happen,
when, for example, the HERE SDK tries too often to resume a download that was paused due to a lost connection.
In general, the HERE SDK will try a few times, before the update is paused.
This error value gives a hint on the reason for the necessary retry operation.
A paused download can be resumed by the user at a later time.
It is 'null' when <code>MapUpdateTask.pauseWithCompaction</code> was called by the user.</li>
</ul>
</section>
<section class="summary source-code" id="source">
<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">void onPause(MapLoaderError? error);</code></pre>
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
<li>/sdk-for-flutter-navigate-maploader-maploader-library</li>
<li>/sdk-for-flutter-navigate-maploader-mapupdateprogresslistener-class</li>
<li class="self-crumb">onPause abstract method</li>
</ol>
<h5>MapUpdateProgressListener class</h5>
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
