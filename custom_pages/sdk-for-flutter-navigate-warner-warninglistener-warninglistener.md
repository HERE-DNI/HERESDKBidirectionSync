---
title: "WarningListener constructor"
slug: "sdk-for-flutter-navigate-warner-warninglistener-warninglistener"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- WarningListener.html -->
<div class="doc-with-sidebar"><div class="doc-content">
<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li>/sdk-for-flutter-navigate</li>
<li>/sdk-for-flutter-navigate-warner-warner-library</li>
<li>/sdk-for-flutter-navigate-warner-warninglistener-class</li>
<li class="self-crumb">WarningListener factory constructor</li>
</ol>
<div class="self-name">WarningListener</div>
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
<div class="main-content" data-above-sidebar="warner/WarningListener-class-sidebar.html" data-below-sidebar="" id="dartdoc-main-content">
<div>
<h1>WarningListener constructor</h1></div>
<section class="multi-line-signature">
WarningListener(<wbr/><ol class="parameter-list single-line"> <li>void onWarningsLambda(<ol class="parameter-list single-line"> <li>List&lt;<wbr/>/sdk-for-flutter-navigate-warner-warning-class&gt;</li>
</ol>)</li>
</ol>)
    </section>
<section class="desc markdown">
<p>A generic listener interface abstract class for receiving warning notifications.</p>
<p>Implementations of this interface are notified whenever the <code>WarnerEngine</code> detects new warnings.
The listener receives a list of <code>Warning</code> objects, each describing a specific event or condition that requires user attention.</p>
<p>Classes interested in warning updates should implement this listener
and register themselves via <code>WarnerEngine.addWarningListener</code>.</p>
<p><strong>Note:</strong> This is a beta release of this feature, so there could be a few bugs and unexpected
behaviors. Related APIs may change for new releases without a deprecation process.</p>
</section>
<section class="summary source-code" id="source">
<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">factory WarningListener(
  void Function(List&lt;Warning&gt;) onWarningsLambda,

) =&gt; WarningListener$Lambdas(
  onWarningsLambda,

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
<li>/sdk-for-flutter-navigate</li>
<li>/sdk-for-flutter-navigate-warner-warner-library</li>
<li>/sdk-for-flutter-navigate-warner-warninglistener-class</li>
<li class="self-crumb">WarningListener factory constructor</li>
</ol>
<h5>WarningListener class</h5>
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
