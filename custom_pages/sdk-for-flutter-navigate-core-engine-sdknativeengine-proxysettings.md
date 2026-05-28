---
title: "proxySettings property"
slug: "sdk-for-flutter-navigate-core-engine-sdknativeengine-proxysettings"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- proxySettings.html -->
<div class="doc-with-sidebar"><div class="doc-content">
<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li>/sdk-for-flutter-navigate</li>
<li>/sdk-for-flutter-navigate-core-engine-core-engine-library</li>
<li>/sdk-for-flutter-navigate-core-engine-sdknativeengine-class</li>
<li class="self-crumb">proxySettings property</li>
</ol>
<div class="self-name">proxySettings</div>
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
<h1>proxySettings property</h1></div>
<section id="getter">
<section class="multi-line-signature">
/sdk-for-flutter-navigate-core-engine-proxysettings-class?
proxySettings
</section>
<section class="desc markdown">
<p>Proxy settings of this SDK engine that will be used by HERE SDK network for all requests.
Defaults to (<code>null</code>), which indicates proxy is not enabled.
When setting proxy settings, they will immediately be applied and all the pending and fresh requests will use these settings.
Pass (<code>null</code>) to indicate that proxy should be disabled.
If proxy is necessary from the start then it's recommended to use /sdk-for-flutter-navigate-core-engine-networksettings-proxysettings in /sdk-for-flutter-navigate-core-engine-sdkoptions-networksettings.</p>
<p><strong>Note:</strong> This is a beta release of this feature, so there could be a few bugs and unexpected behaviors.
Related APIs may change for new releases without a deprecation process.
Gets the current proxy settings.</p>
</section>
<section class="summary source-code" id="source">
<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">ProxySettings? get proxySettings;</code></pre>
</section>
</section>
<section id="setter">
<section class="multi-line-signature">
void
proxySettings=(<wbr/>/sdk-for-flutter-navigate-core-engine-proxysettings-class? value)
</section>
<section class="desc markdown">
<p>Proxy settings of this SDK engine that will be used by HERE SDK network for all requests.
Defaults to (<code>null</code>), which indicates proxy is not enabled.
When setting proxy settings, they will immediately be applied and all the pending and fresh requests will use these settings.
Pass (<code>null</code>) to indicate that proxy should be disabled.
If proxy is necessary from the start then it's recommended to use /sdk-for-flutter-navigate-core-engine-networksettings-proxysettings in /sdk-for-flutter-navigate-core-engine-sdkoptions-networksettings.</p>
<p><strong>Note:</strong> This is a beta release of this feature, so there could be a few bugs and unexpected behaviors.
Related APIs may change for new releases without a deprecation process.
Sets the proxy settings.</p>
</section>
<section class="summary source-code" id="source">
<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">set proxySettings(ProxySettings? value);</code></pre>
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
<li>/sdk-for-flutter-navigate</li>
<li>/sdk-for-flutter-navigate-core-engine-core-engine-library</li>
<li>/sdk-for-flutter-navigate-core-engine-sdknativeengine-class</li>
<li class="self-crumb">proxySettings property</li>
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
