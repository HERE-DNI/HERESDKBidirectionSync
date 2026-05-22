---
title: "Untitled"
slug: "sdk-for-flutter-navigate-warner-warninglistener-class"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- WarningListener-class.html -->

<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li>/sdk-for-flutter-navigate</li>
<li>/sdk-for-flutter-navigate-warner-warner-library</li>
<li class="self-crumb">WarningListener class</li>
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
<div class="main-content" data-above-sidebar="warner/warner-library-sidebar.html" data-below-sidebar="warner/WarningListener-class-sidebar.html" id="dartdoc-main-content">
<div>
<h1>WarningListener class abstract</h1></div>
<section class="desc markdown">
<p>A generic listener interface abstract class for receiving warning notifications.</p>
<p>Implementations of this interface are notified whenever the <code>WarnerEngine</code> detects new warnings.
The listener receives a list of <code>Warning</code> objects, each describing a specific event or condition that requires user attention.</p>
<p>Classes interested in warning updates should implement this listener
and register themselves via <code>WarnerEngine.addWarningListener</code>.</p>
<p><strong>Note:</strong> This is a beta release of this feature, so there could be a few bugs and unexpected
behaviors. Related APIs may change for new releases without a deprecation process.</p>
</section>
<section class="summary offset-anchor" id="constructors">
<h2>Constructors</h2>
<dl class="constructor-summary-list">
<dt class="callable" id="WarningListener">
/sdk-for-flutter-navigate-warner-warninglistener-warninglistener(void onWarningsLambda(List&lt;<wbr/>/sdk-for-flutter-navigate-warner-warning-class&gt;))
</dt>
<dd>
          A generic listener interface abstract class for receiving warning notifications.
            <div class="constructor-modifier features">factory</div>
</dd>
</dl>
</section>
<section class="summary offset-anchor inherited" id="instance-properties">
<h2>Properties</h2>
<dl class="properties">
<dt class="property inherited" id="hashCode">
/sdk-for-flutter-navigate-warner-warninglistener-hashcode
→ int
</dt>
<dd class="inherited">
  The hash code for this object.
  <div class="features">no setterinherited</div>
</dd>
<dt class="property inherited" id="runtimeType">
/sdk-for-flutter-navigate-warner-warninglistener-runtimetype
→ Type
</dt>
<dd class="inherited">
  A representation of the runtime type of the object.
  <div class="features">no setterinherited</div>
</dd>
</dl>
</section>
<section class="summary offset-anchor" id="instance-methods">
<h2>Methods</h2>
<dl class="callables">
<dt class="callable inherited" id="noSuchMethod">
/sdk-for-flutter-navigate-warner-warninglistener-nosuchmethod(<wbr/>Invocation invocation)
    → dynamic

</dt>
<dd class="inherited">
  Invoked when a nonexistent method or property is accessed.
  <div class="features">inherited</div>
</dd>
<dt class="callable" id="onWarnings">
/sdk-for-flutter-navigate-warner-warninglistener-onwarnings(<wbr/>List&lt;<wbr/>/sdk-for-flutter-navigate-warner-warning-class&gt; warnings)
    → void

</dt>
<dd>
  Called when a new warnings is detected.
  

</dd>
<dt class="callable inherited" id="toString">
/sdk-for-flutter-navigate-warner-warninglistener-tostring(<wbr/>)
    → String

</dt>
<dd class="inherited">
  A string representation of this object.
  <div class="features">inherited</div>
</dd>
</dl>
</section>
<section class="summary offset-anchor inherited" id="operators">
<h2>Operators</h2>
<dl class="callables">
<dt class="callable inherited" id="operator ==">
/sdk-for-flutter-navigate-warner-warninglistener-operator-equals(<wbr/>Object other)
    → bool

</dt>
<dd class="inherited">
  The equality operator.
  <div class="features">inherited</div>
</dd>
</dl>
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
<li class="self-crumb">WarningListener class</li>
</ol>
<h5>warner library</h5>
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
