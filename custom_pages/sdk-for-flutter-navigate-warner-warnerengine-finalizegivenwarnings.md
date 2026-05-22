---
title: "Untitled"
slug: "sdk-for-flutter-navigate-warner-warnerengine-finalizegivenwarnings"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- finalizeGivenWarnings.html -->

<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li>/sdk-for-flutter-navigate</li>
<li>/sdk-for-flutter-navigate-warner-warner-library</li>
<li>/sdk-for-flutter-navigate-warner-warnerengine-class</li>
<li class="self-crumb">finalizeGivenWarnings abstract method</li>
</ol>
<div class="self-name">finalizeGivenWarnings</div>
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
<div class="main-content" data-above-sidebar="warner/WarnerEngine-class-sidebar.html" data-below-sidebar="" id="dartdoc-main-content">
<div>
<h1>finalizeGivenWarnings abstract method</h1></div>
<section class="multi-line-signature">
void
finalizeGivenWarnings(<wbr/>)

      

    </section>
<section class="desc markdown">
<p>Marks all currently active warnings as passed (<code>DistanceType.PASSED</code>), notifies all
registered /sdk-for-flutter-navigate-warner-warninglistener-class instances on the main thread, and then clears these
warnings from their corresponding registries by invoking the appropriate<code>WarningsRegistry.clear&lt;Type&gt;</code> methods.</p>
<p>This method triggers notifications only for enabled warners. Warning processing may
occur asynchronously unless synchronous mode is enabled.</p>
<p><strong>Note</strong>: Although each warning type can also be cleared manually via the respective
<code>WarningsRegistry.clear&lt;Type&gt;()</code> methods, <code>finalizeGivenWarnings()</code> provides a
unified way to flush all active warnings after they have been reported as
passed. If this method is not invoked, warnings will continue to accumulate in the
registry according to the configured warning-generation options.</p>
</section>
<section class="summary source-code" id="source">
<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">void finalizeGivenWarnings();</code></pre>
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
<li>/sdk-for-flutter-navigate-warner-warner-library</li>
<li>/sdk-for-flutter-navigate-warner-warnerengine-class</li>
<li class="self-crumb">finalizeGivenWarnings abstract method</li>
</ol>
<h5>WarnerEngine class</h5>
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
