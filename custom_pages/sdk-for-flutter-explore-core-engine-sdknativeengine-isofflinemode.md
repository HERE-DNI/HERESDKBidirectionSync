---
title: "isOfflineMode property"
slug: "sdk-for-flutter-explore-core-engine-sdknativeengine-isofflinemode"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- isOfflineMode.html -->
<div class="doc-with-sidebar"><div class="doc-content">
<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li>/sdk-for-flutter-explore</li>
<li>/sdk-for-flutter-explore-core-engine-core-engine-library</li>
<li>/sdk-for-flutter-explore-core-engine-sdknativeengine-class</li>
<li class="self-crumb">isOfflineMode property</li>
</ol>
<div class="self-name">isOfflineMode</div>
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
<h1>isOfflineMode property</h1></div>
<section id="getter">
<section class="multi-line-signature">
bool
isOfflineMode
</section>
<section class="desc markdown">
<p>The offline mode.
Sets offline mode for the HERE SDK to offline or online.
Defaults to false, which means the HERE SDK uses an online connection.
When enabled, this prevents the HERE SDK from initiating any online connection except for provided pass through features if set.
See /sdk-for-flutter-explore-core-engine-sdknativeengine-passthroughfeatures.
Note that the flag does not cancel pending requests.
The mode can be enabled or disabled at any time. In order to fully operate offline, the mode
needs to be enabled via /sdk-for-flutter-explore-core-engine-sdkoptions-offlinemode.
Initialization of the HERE SDK itself does not require an internet connection.
Returns <code>true</code> if the HERE SDK uses offline connection mode, otherwise returns <code>false</code>.</p>
<p>Note: This is a <strong>beta</strong> release of this feature, so there could be a few bugs and unexpected behaviors.
Related APIs may change for new releases without a deprecation process.
Gets the current offline mode.</p>
</section>
<section class="summary source-code" id="source">
<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">bool get isOfflineMode;</code></pre>
</section>
</section>
<section id="setter">
<section class="multi-line-signature">
void
isOfflineMode=(<wbr/>bool value)
</section>
<section class="desc markdown">
<p>The offline mode.
Sets offline mode for the HERE SDK to offline or online.
Defaults to false, which means the HERE SDK uses an online connection.
When enabled, this prevents the HERE SDK from initiating any online connection except for provided pass through features if set.
See /sdk-for-flutter-explore-core-engine-sdknativeengine-passthroughfeatures.
Note that the flag does not cancel pending requests.
The mode can be enabled or disabled at any time. In order to fully operate offline, the mode
needs to be enabled via /sdk-for-flutter-explore-core-engine-sdkoptions-offlinemode.
Initialization of the HERE SDK itself does not require an internet connection.
Returns <code>true</code> if the HERE SDK uses offline connection mode, otherwise returns <code>false</code>.</p>
<p>Note: This is a <strong>beta</strong> release of this feature, so there could be a few bugs and unexpected behaviors.
Related APIs may change for new releases without a deprecation process.
Sets the offline mode.</p>
</section>
<section class="summary source-code" id="source">
<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">set isOfflineMode(bool value);</code></pre>
</section>
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
<li class="self-crumb">isOfflineMode property</li>
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
</div></div>
</div>
`
}</HTMLBlock>
