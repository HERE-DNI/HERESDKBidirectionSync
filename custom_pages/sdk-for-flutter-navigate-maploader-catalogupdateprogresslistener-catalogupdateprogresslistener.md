---
title: "Untitled"
slug: "sdk-for-flutter-navigate-maploader-catalogupdateprogresslistener-catalogupdateprogresslistener"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- CatalogUpdateProgressListener.html -->

<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li>/sdk-for-flutter-navigate</li>
<li>/sdk-for-flutter-navigate-maploader-maploader-library</li>
<li>/sdk-for-flutter-navigate-maploader-catalogupdateprogresslistener-class</li>
<li class="self-crumb">CatalogUpdateProgressListener factory constructor</li>
</ol>
<div class="self-name">CatalogUpdateProgressListener</div>
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
<div class="main-content" data-above-sidebar="maploader/CatalogUpdateProgressListener-class-sidebar.html" data-below-sidebar="" id="dartdoc-main-content">
<div>
<h1>CatalogUpdateProgressListener constructor</h1></div>
<section class="multi-line-signature">
CatalogUpdateProgressListener(<wbr/><ol class="parameter-list"> <li>void onProgressLambda(<ol class="parameter-list single-line"> <li>/sdk-for-flutter-navigate-maploader-regionid-class, </li>
<li>int</li>
</ol>), </li>
<li>void onPauseLambda(<ol class="parameter-list single-line"> <li>/sdk-for-flutter-navigate-maploader-maploadererror?</li>
</ol>), </li>
<li>void onCompleteLambda(<ol class="parameter-list single-line"> <li>/sdk-for-flutter-navigate-maploader-maploadererror?</li>
</ol>), </li>
<li>void onResumeLambda(), </li>
</ol>)
    </section>
<section class="desc markdown">
<p>Abstract class to get notified on status updates
when updating catalog, previously downloaded by /sdk-for-flutter-navigate-maploader-mapdownloader-class.</p>
</section>
<section class="summary source-code" id="source">
<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">factory CatalogUpdateProgressListener(
  void Function(RegionId, int) onProgressLambda,
  void Function(MapLoaderError?) onPauseLambda,
  void Function(MapLoaderError?) onCompleteLambda,
  void Function() onResumeLambda,

) =&gt; CatalogUpdateProgressListener$Lambdas(
  onProgressLambda,
  onPauseLambda,
  onCompleteLambda,
  onResumeLambda,

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
<li>/sdk-for-flutter-navigate-maploader-maploader-library</li>
<li>/sdk-for-flutter-navigate-maploader-catalogupdateprogresslistener-class</li>
<li class="self-crumb">CatalogUpdateProgressListener factory constructor</li>
</ol>
<h5>CatalogUpdateProgressListener class</h5>
<div id="dartdoc-sidebar-left-content"></div>
</div>
<div class="sidebar sidebar-offcanvas-right" id="dartdoc-sidebar-right">
</div>
</main>
<footer>

    here_sdk
      4.26.0
  
</footer>



</div>
`
}</HTMLBlock>
