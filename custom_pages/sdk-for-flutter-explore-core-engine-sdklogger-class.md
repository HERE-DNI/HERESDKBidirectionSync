---
title: "Constructors"
slug: "sdk-for-flutter-explore-core-engine-sdklogger-class"
---

<HTMLBlock>
<div class="sdk-for-flutter">
<!-- SDKLogger-class.html -->
<div class="doc-with-sidebar"><div class="sidebar-nav"><ol>
<li class="section-title"><a href="core.engine/SDKLogger-class.html#constructors">Constructors</a></li>
<li><a href="core.engine/SDKLogger/SDKLogger.html">SDKLogger</a></li>
<li class="section-title inherited">
<a href="core.engine/SDKLogger-class.html#instance-properties">Properties</a>
</li>
<li class="inherited"><a href="core.engine/SDKLogger/hashCode.html">hashCode</a></li>
<li class="inherited"><a href="core.engine/SDKLogger/runtimeType.html">runtimeType</a></li>
<li class="section-title inherited"><a href="core.engine/SDKLogger-class.html#instance-methods">Methods</a></li>
<li class="inherited"><a href="core.engine/SDKLogger/noSuchMethod.html">noSuchMethod</a></li>
<li class="inherited"><a href="core.engine/SDKLogger/toString.html">toString</a></li>
<li class="section-title inherited"><a href="core.engine/SDKLogger-class.html#operators">Operators</a></li>
<li class="inherited"><a href="core.engine/SDKLogger/operator_equals.html">operator ==</a></li>
<li class="section-title"><a href="core.engine/SDKLogger-class.html#static-methods">Static methods</a></li>
<li><a href="core.engine/SDKLogger/error.html">error</a></li>
<li><a href="core.engine/SDKLogger/fatal.html">fatal</a></li>
<li><a href="core.engine/SDKLogger/info.html">info</a></li>
<li><a href="core.engine/SDKLogger/log.html">log</a></li>
<li><a href="core.engine/SDKLogger/warn.html">warn</a></li>
</ol></div><div class="doc-content">
<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li><a href="../index.html">/sdk-for-flutter-explore</a></li>
<li><a href="../core.engine/core.engine-library.html">/sdk-for-flutter-explore-core-engine-core-engine-library</a></li>
<li class="self-crumb">SDKLogger class</li>
</ol>
<div class="self-name">SDKLogger</div>
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
<div class="main-content" data-above-sidebar="core.engine/core.engine-library-sidebar.html" data-below-sidebar="core.engine/SDKLogger-class-sidebar.html" id="dartdoc-main-content">
<div>
<h1>SDKLogger class abstract</h1></div>
<section class="desc markdown">
<p>Logging interface for Android/iOS platforms.</p>
<p>These logs are under management of <a href="../core.engine/LogControl-class.html">/sdk-for-flutter-explore-core-engine-logcontrol-class</a> and should be used instead of platform-specific logging functions.</p>
</section>
<section class="summary offset-anchor" id="constructors">
<h2>Constructors</h2>
<dl class="constructor-summary-list">
<dt class="callable" id="SDKLogger">
<a href="../core.engine/SDKLogger/SDKLogger.html">/sdk-for-flutter-explore-core-engine-sdklogger-sdklogger</a>()
</dt>
<dd>
</dd>
</dl>
</section>
<section class="summary offset-anchor inherited" id="instance-properties">
<h2>Properties</h2>
<dl class="properties">
<dt class="property inherited" id="hashCode">
<a href="../core.engine/SDKLogger/hashCode.html">/sdk-for-flutter-explore-core-engine-sdklogger-hashcode</a>
→ int
</dt>
<dd class="inherited">
  The hash code for this object.
  <div class="features">no setterinherited</div>
</dd>
<dt class="property inherited" id="runtimeType">
<a href="../core.engine/SDKLogger/runtimeType.html">/sdk-for-flutter-explore-core-engine-sdklogger-runtimetype</a>
→ Type
</dt>
<dd class="inherited">
  A representation of the runtime type of the object.
  <div class="features">no setterinherited</div>
</dd>
</dl>
</section>
<section class="summary offset-anchor inherited" id="instance-methods">
<h2>Methods</h2>
<dl class="callables">
<dt class="callable inherited" id="noSuchMethod">
<a href="../core.engine/SDKLogger/noSuchMethod.html">/sdk-for-flutter-explore-core-engine-sdklogger-nosuchmethod</a>(<wbr/>Invocation invocation)
    → dynamic

</dt>
<dd class="inherited">
  Invoked when a nonexistent method or property is accessed.
  <div class="features">inherited</div>
</dd>
<dt class="callable inherited" id="toString">
<a href="../core.engine/SDKLogger/toString.html">/sdk-for-flutter-explore-core-engine-sdklogger-tostring</a>(<wbr/>)
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
<a href="../core.engine/SDKLogger/operator_equals.html">/sdk-for-flutter-explore-core-engine-sdklogger-operator-equals</a>(<wbr/>Object other)
    → bool

</dt>
<dd class="inherited">
  The equality operator.
  <div class="features">inherited</div>
</dd>
</dl>
</section>
<section class="summary offset-anchor" id="static-methods">
<h2>Static Methods</h2>
<dl class="callables">
<dt class="callable" id="error">
<a href="../core.engine/SDKLogger/error.html">/sdk-for-flutter-explore-core-engine-sdklogger-error</a>(<wbr/>String tag, String message)
    → void

</dt>
<dd>
  convenient function to print a message with log level ERROR and tag.
  

</dd>
<dt class="callable" id="fatal">
<a href="../core.engine/SDKLogger/fatal.html">/sdk-for-flutter-explore-core-engine-sdklogger-fatal</a>(<wbr/>String tag, String message)
    → void

</dt>
<dd>
  convenient function to print a message with log level FATAL and tag.
  

</dd>
<dt class="callable" id="info">
<a href="../core.engine/SDKLogger/info.html">/sdk-for-flutter-explore-core-engine-sdklogger-info</a>(<wbr/>String tag, String message)
    → void

</dt>
<dd>
  convenient function to print a message with log level INFO and tag.
  

</dd>
<dt class="callable" id="log">
<a href="../core.engine/SDKLogger/log.html">/sdk-for-flutter-explore-core-engine-sdklogger-log</a>(<wbr/><a href="../core.engine/LogLevel.html">/sdk-for-flutter-explore-core-engine-loglevel</a> level, String tag, String message)
    → void

</dt>
<dd>
<li>
<p><code>level</code> The severity of the log message.</p>
</li>
<li>
<p><code>tag</code> The log tag.</p>
</li>
<li>
<p><code>message</code> The log message.</p>
</li>
</dd>
<dt class="callable" id="warn">
<a href="../core.engine/SDKLogger/warn.html">/sdk-for-flutter-explore-core-engine-sdklogger-warn</a>(<wbr/>String tag, String message)
    → void

</dt>
<dd>
  convenient function to print a message with log level WARNING and tag.
  

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
<li><a href="../index.html">/sdk-for-flutter-explore</a></li>
<li><a href="../core.engine/core.engine-library.html">/sdk-for-flutter-explore-core-engine-core-engine-library</a></li>
<li class="self-crumb">SDKLogger class</li>
</ol>
<h5>core.engine library</h5>
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
</HTMLBlock>
