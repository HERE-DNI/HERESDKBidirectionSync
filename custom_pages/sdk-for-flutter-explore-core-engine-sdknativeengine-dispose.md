---
title: "Untitled"
slug: "sdk-for-flutter-explore-core-engine-sdknativeengine-dispose"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- dispose.html -->

<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li>/sdk-for-flutter-explore</li>
<li>/sdk-for-flutter-explore-core-engine-core-engine-library</li>
<li>/sdk-for-flutter-explore-core-engine-sdknativeengine-class</li>
<li class="self-crumb">dispose abstract method</li>
</ol>
<div class="self-name">dispose</div>
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
<div class="main-content" data-above-sidebar="core.engine/SDKNativeEngine-class-sidebar.html" data-below-sidebar="" id="dartdoc-main-content">
<div>
<h1>dispose abstract method</h1></div>
<section class="multi-line-signature">
Future&lt;<wbr/>void&gt;
dispose(<wbr/>)

      

    </section>
<section class="desc markdown">
<p>Stops pending requests and closes open files and databases in main thread.</p>
<p>Dispose signal is sent to dependent modules.
Usage of engine, or dependent modules after calling dispose leads to undefined behavior.
Please be aware that this method does not clean any type of storage.
<strong>Note:</strong>
This method should be called from main thread.</p>
</section>
<section class="summary source-code" id="source">
<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">Future&lt;void&gt; dispose();</code></pre>
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
<li>/sdk-for-flutter-explore-core-engine-core-engine-library</li>
<li>/sdk-for-flutter-explore-core-engine-sdknativeengine-class</li>
<li class="self-crumb">dispose abstract method</li>
</ol>
<h5>SDKNativeEngine class</h5>
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
