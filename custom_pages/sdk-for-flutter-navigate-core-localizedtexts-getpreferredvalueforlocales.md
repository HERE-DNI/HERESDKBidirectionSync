---
title: "getPreferredValueForLocales method"
slug: "sdk-for-flutter-navigate-core-localizedtexts-getpreferredvalueforlocales"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- getPreferredValueForLocales.html -->
<div class="doc-with-sidebar"><div class="doc-content">
<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li>/sdk-for-flutter-navigate</li>
<li>/sdk-for-flutter-navigate-core-core-library</li>
<li>/sdk-for-flutter-navigate-core-localizedtexts-class</li>
<li class="self-crumb">getPreferredValueForLocales method</li>
</ol>
<div class="self-name">getPreferredValueForLocales</div>
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
<div class="main-content" data-above-sidebar="core/LocalizedTexts-class-sidebar.html" data-below-sidebar="" id="dartdoc-main-content">
<div>
<h1>getPreferredValueForLocales method</h1></div>
<section class="multi-line-signature">
String?
getPreferredValueForLocales(<wbr/><ol class="parameter-list single-line"> <li>List&lt;<wbr/><a href="https://pub.dev/documentation/intl/0.20.2/locale/Locale-class.html">Locale</a>&gt; locales</li>
</ol>)

      

    </section>
<section class="desc markdown">
<p>Returns best name or title to be presented to the user according to specified
locales.</p>
<p>The locales are expected to be ordered by priority.
If no matching locale found - the default is returned.
In case of empty list returns <code>null</code>.</p>
<ul>
<li><code>locales</code> Locales that will be used to translate name or title.</li>
</ul>
<p>Returns <code>String?</code>. Returns best name or title to be presented to the user according to specified locales.</p>
</section>
<section class="summary source-code" id="source">
<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">String? getPreferredValueForLocales(List&lt;Locale&gt; locales) =&gt; $prototype.getPreferredValueForLocales(this, locales);</code></pre>
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
<li>/sdk-for-flutter-navigate-core-core-library</li>
<li>/sdk-for-flutter-navigate-core-localizedtexts-class</li>
<li class="self-crumb">getPreferredValueForLocales method</li>
</ol>
<h5>LocalizedTexts class</h5>
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
