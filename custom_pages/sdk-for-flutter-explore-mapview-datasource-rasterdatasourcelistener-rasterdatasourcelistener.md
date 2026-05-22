---
title: "Untitled"
slug: "sdk-for-flutter-explore-mapview-datasource-rasterdatasourcelistener-rasterdatasourcelistener"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- RasterDataSourceListener.html -->

<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li>/sdk-for-flutter-explore</li>
<li>/sdk-for-flutter-explore-mapview-datasource-mapview-datasource-library</li>
<li>/sdk-for-flutter-explore-mapview-datasource-rasterdatasourcelistener-class</li>
<li class="self-crumb">RasterDataSourceListener factory constructor</li>
</ol>
<div class="self-name">RasterDataSourceListener</div>
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
<div class="main-content" data-above-sidebar="mapview.datasource/RasterDataSourceListener-class-sidebar.html" data-below-sidebar="" id="dartdoc-main-content">
<div>
<h1>RasterDataSourceListener constructor</h1></div>
<section class="multi-line-signature">
RasterDataSourceListener(<wbr/><ol class="parameter-list single-line"> <li>void onRasterDataSourceReadyLambda(), </li>
<li>void onRasterDataSourceErrorLambda(<ol class="parameter-list single-line"> <li>/sdk-for-flutter-explore-mapview-datasource-rasterdatasourceerror</li>
</ol>)</li>
</ol>)
    </section>
<section class="desc markdown">
<p>Listener for RasterDataSource events.</p>
</section>
<section class="summary source-code" id="source">
<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">factory RasterDataSourceListener(
  void Function() onRasterDataSourceReadyLambda,
  void Function(RasterDataSourceError) onRasterDataSourceErrorLambda,

) =&gt; RasterDataSourceListener$Lambdas(
  onRasterDataSourceReadyLambda,
  onRasterDataSourceErrorLambda,

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
<li>/sdk-for-flutter-explore</li>
<li>/sdk-for-flutter-explore-mapview-datasource-mapview-datasource-library</li>
<li>/sdk-for-flutter-explore-mapview-datasource-rasterdatasourcelistener-class</li>
<li class="self-crumb">RasterDataSourceListener factory constructor</li>
</ol>
<h5>RasterDataSourceListener class</h5>
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
