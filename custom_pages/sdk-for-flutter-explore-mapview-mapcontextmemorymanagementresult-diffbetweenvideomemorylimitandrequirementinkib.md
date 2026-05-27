---
title: "Implementation"
slug: "sdk-for-flutter-explore-mapview-mapcontextmemorymanagementresult-diffbetweenvideomemorylimitandrequirementinkib"
---

<HTMLBlock>
<div class="sdk-for-flutter">
<!-- diffBetweenVideoMemoryLimitAndRequirementInKiB.html -->
<div class="doc-with-sidebar"><div class="doc-content">
<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li><a href="../../index.html">/sdk-for-flutter-explore</a></li>
<li><a href="../../mapview/mapview-library.html">/sdk-for-flutter-explore-mapview-mapview-library</a></li>
<li><a href="../../mapview/MapContextMemoryManagementResult-class.html">/sdk-for-flutter-explore-mapview-mapcontextmemorymanagementresult-class</a></li>
<li class="self-crumb">diffBetweenVideoMemoryLimitAndRequirementInKiB property</li>
</ol>
<div class="self-name">diffBetweenVideoMemoryLimitAndRequirementInKiB</div>
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
<div class="main-content" data-above-sidebar="mapview/MapContextMemoryManagementResult-class-sidebar.html" data-below-sidebar="" id="dartdoc-main-content">
<div>
<h1>diffBetweenVideoMemoryLimitAndRequirementInKiB property</h1></div>
<section class="multi-line-signature">
        
        int?
        diffBetweenVideoMemoryLimitAndRequirementInKiB
<div class="features">getter/setter pair</div>
</section>
<section class="desc markdown">
<p>The difference in kibibytes between the limit and the video-memory requirement
for only the currently visible data. If positive, the returned value is the surplus
value over the currently required bare minimum. Even when positive, if the limit set
is low, the application could later breach the limit and delete even visible data.
A non positive value means the limit cannot fit the existing visible data and there could
be data disappearing or flickering. If for some reason the callback is ignored or
correct memory limit cannot be calculated, <code>null</code> value is returned.</p>
</section>
<section class="summary source-code" id="source">
<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">int? diffBetweenVideoMemoryLimitAndRequirementInKiB;</code></pre>
</section>
</div>
<div class="sidebar sidebar-offcanvas-left" id="dartdoc-sidebar-left">
<header class="hidden-l" id="header-search-sidebar">
<form class="search-sidebar" role="search">
<input autocomplete="off" class="form-control typeahead" disabled="" id="search-sidebar" placeholder="Loading search..." type="text"/>
</form>
</header>
<ol class="breadcrumbs gt-separated dark hidden-l" id="sidebar-nav">
<li><a href="../../index.html">/sdk-for-flutter-explore</a></li>
<li><a href="../../mapview/mapview-library.html">/sdk-for-flutter-explore-mapview-mapview-library</a></li>
<li><a href="../../mapview/MapContextMemoryManagementResult-class.html">/sdk-for-flutter-explore-mapview-mapcontextmemorymanagementresult-class</a></li>
<li class="self-crumb">diffBetweenVideoMemoryLimitAndRequirementInKiB property</li>
</ol>
<h5>MapContextMemoryManagementResult class</h5>
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
</HTMLBlock>
