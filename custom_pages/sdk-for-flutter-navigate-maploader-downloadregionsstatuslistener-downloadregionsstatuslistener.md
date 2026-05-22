---
title: "Untitled"
slug: "sdk-for-flutter-navigate-maploader-downloadregionsstatuslistener-downloadregionsstatuslistener"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- DownloadRegionsStatusListener.html -->

<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li>/sdk-for-flutter-navigate</li>
<li>/sdk-for-flutter-navigate-maploader-maploader-library</li>
<li>/sdk-for-flutter-navigate-maploader-downloadregionsstatuslistener-class</li>
<li class="self-crumb">DownloadRegionsStatusListener factory constructor</li>
</ol>
<div class="self-name">DownloadRegionsStatusListener</div>
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
<div class="main-content" data-above-sidebar="maploader/DownloadRegionsStatusListener-class-sidebar.html" data-below-sidebar="" id="dartdoc-main-content">
<div>
<h1>DownloadRegionsStatusListener constructor</h1></div>
<section class="multi-line-signature">
DownloadRegionsStatusListener(<wbr/><ol class="parameter-list"> <li>void onDownloadRegionsCompleteLambda(<ol class="parameter-list single-line"> <li>/sdk-for-flutter-navigate-maploader-maploadererror?, </li>
<li>List&lt;<wbr/>/sdk-for-flutter-navigate-maploader-regionid-class&gt;?</li>
</ol>), </li>
<li>void onProgressLambda(<ol class="parameter-list single-line"> <li>/sdk-for-flutter-navigate-maploader-regionid-class, </li>
<li>int</li>
</ol>), </li>
<li>void onPauseLambda(<ol class="parameter-list single-line"> <li>/sdk-for-flutter-navigate-maploader-maploadererror?</li>
</ol>), </li>
<li>void onResumeLambda(), </li>
</ol>)
    </section>
<section class="desc markdown">
<p>Abstract class to get notified on
status updates when downloading map regions.</p>
</section>
<section class="summary source-code" id="source">
<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">factory DownloadRegionsStatusListener(
  void Function(MapLoaderError?, List&lt;RegionId&gt;?) onDownloadRegionsCompleteLambda,
  void Function(RegionId, int) onProgressLambda,
  void Function(MapLoaderError?) onPauseLambda,
  void Function() onResumeLambda,

) =&gt; DownloadRegionsStatusListener$Lambdas(
  onDownloadRegionsCompleteLambda,
  onProgressLambda,
  onPauseLambda,
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
<li>/sdk-for-flutter-navigate-maploader-downloadregionsstatuslistener-class</li>
<li class="self-crumb">DownloadRegionsStatusListener factory constructor</li>
</ol>
<h5>DownloadRegionsStatusListener class</h5>
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
