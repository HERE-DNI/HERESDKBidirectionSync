---
title: "Untitled"
slug: "sdk-for-flutter-explore-core-engine-sdknativeengine-makesharedinstance"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- makeSharedInstance.html -->

<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li>/sdk-for-flutter-explore</li>
<li>/sdk-for-flutter-explore-core-engine-core-engine-library</li>
<li>/sdk-for-flutter-explore-core-engine-sdknativeengine-class</li>
<li class="self-crumb">makeSharedInstance static method</li>
</ol>
<div class="self-name">makeSharedInstance</div>
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
<h1>makeSharedInstance static method</h1></div>
<section class="multi-line-signature">
Future&lt;<wbr/>void&gt;
makeSharedInstance(<wbr/><ol class="parameter-list single-line"> <li>/sdk-for-flutter-explore-core-engine-sdkoptions-class options</li>
</ol>)

      

    </section>
<section class="desc markdown">
<p>Makes a new instance of SDKNativeEngine using supplied options and stores it as shared instance
see /sdk-for-flutter-explore-core-engine-sdknativeengine-sharedinstance.</p>
<p>If there was previously shared instance
then it's disposed (see /sdk-for-flutter-explore-core-engine-sdknativeengine-dispose)
before new instance is created.</p>
<ul>
<li><code>options</code> The options for the new engine.</li>
</ul>
<p>Throws /sdk-for-flutter-explore-core-errors-instantiationexception-class. Indicates what went wrong when the instantiation was attempted.</p>
</section>
<section class="summary source-code" id="source">
<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">static Future&lt;void&gt; makeSharedInstance(SDKOptions options) =&gt; $prototype.makeSharedInstance(options);</code></pre>
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
<li class="self-crumb">makeSharedInstance static method</li>
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
