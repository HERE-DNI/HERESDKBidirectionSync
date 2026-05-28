---
title: "getCustomWarning abstract method"
slug: "sdk-for-flutter-navigate-warner-warningsregistry-getcustomwarning"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- getCustomWarning.html -->
<div class="doc-with-sidebar"><div class="doc-content">
<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li>/sdk-for-flutter-navigate</li>
<li>/sdk-for-flutter-navigate-warner-warner-library</li>
<li>/sdk-for-flutter-navigate-warner-warningsregistry-class</li>
<li class="self-crumb">getCustomWarning abstract method</li>
</ol>
<div class="self-name">getCustomWarning</div>
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
<div class="main-content" data-above-sidebar="warner/WarningsRegistry-class-sidebar.html" data-below-sidebar="" id="dartdoc-main-content">
<div>
<h1>getCustomWarning abstract method</h1></div>
<section class="multi-line-signature">
/sdk-for-flutter-navigate-warner-customwarning-class?
getCustomWarning(<wbr/><ol class="parameter-list single-line"> <li>/sdk-for-flutter-navigate-warner-warning-class warning</li>
</ol>)

      

    </section>
<section class="desc markdown">
<p>Returns additional data associated with the given custom warning.</p>
<p>The provided <code>WarningsRegistry.getCustomWarning.warning</code> identifies a specific custom warning instance by its
base warning information and custom warning type. This information is used
to resolve the corresponding entry in the warning registry and retrieve
any additional, type-specific data associated with the warning.</p>
<ul>
<li><code>warning</code> The /sdk-for-flutter-navigate-warner-warning-class instance identifying the custom warning for which
additional data should be retrieved.</li>
</ul>
<p>Returns /sdk-for-flutter-navigate-warner-customwarning-class. The <code>CustomWarning</code> associated with the given <code>WarningsRegistry.getCustomWarning.warning</code>, or <code>null</code>
if no additional data exists for this warning.
The returned object contains the payload with type-specific
details and attributes of the corresponding warning.</p>
<p><strong>Note:</strong> This is a beta release of this feature, so there could be a few bugs and unexpected
behaviors. Related APIs may change for new releases without a deprecation process.</p>
</section>
<section class="summary source-code" id="source">
<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">CustomWarning? getCustomWarning(Warning warning);</code></pre>
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
<li>/sdk-for-flutter-navigate-warner-warningsregistry-class</li>
<li class="self-crumb">getCustomWarning abstract method</li>
</ol>
<h5>WarningsRegistry class</h5>
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
