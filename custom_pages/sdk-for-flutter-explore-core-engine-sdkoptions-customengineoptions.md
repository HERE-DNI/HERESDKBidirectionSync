---
title: "Untitled"
slug: "sdk-for-flutter-explore-core-engine-sdkoptions-customengineoptions"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- customEngineOptions.html -->

<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li>/sdk-for-flutter-explore</li>
<li>/sdk-for-flutter-explore-core-engine-core-engine-library</li>
<li>/sdk-for-flutter-explore-core-engine-sdkoptions-class</li>
<li class="self-crumb">customEngineOptions property</li>
</ol>
<div class="self-name">customEngineOptions</div>
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
<div class="main-content" data-above-sidebar="core.engine/SDKOptions-class-sidebar.html" data-below-sidebar="" id="dartdoc-main-content">
<div>
<h1>customEngineOptions property</h1></div>
<section class="multi-line-signature">
        
        Map&lt;<wbr/>/sdk-for-flutter-explore-core-engine-enginebaseurl, /sdk-for-flutter-explore-core-engine-engineoptions-class&gt;
customEngineOptions
<div class="features">getter/setter pair</div>
</section>
<section class="desc markdown">
<p>Set custom options for SDK Engines. This includes:</p>
<ul>
<li><code>custom_base_url</code>: Allows engines to use custom base URLs for alternative services.
By default, the available endpoints use HERE backend endpoints.
If unsupported base URLs are specified, the related features will become non-functional.
Please contact your HERE representative to learn about possible custom base URL usage options.</li>
<li><code>custom_authentication_mode</code>: Enables bearer authentication mode for engines,
which adds or omits the header ("Authorization", "Bearer $Token") to each
online request made by the module the object is added to.
The token (if used) can be provided directly or retrieved via key/secret
from a dedicated backend.
Note: This is a beta release of this feature, so there could be a few bugs and unexpected behaviors.
Related APIs may change for new releases without a deprecation process.</li>
</ul>
</section>
<section class="summary source-code" id="source">
<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">Map&lt;EngineBaseURL, EngineOptions&gt; customEngineOptions;</code></pre>
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
<li>/sdk-for-flutter-explore-core-engine-sdkoptions-class</li>
<li class="self-crumb">customEngineOptions property</li>
</ol>
<h5>SDKOptions class</h5>
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
