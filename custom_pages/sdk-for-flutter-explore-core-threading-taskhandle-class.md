---
title: "Constructors"
slug: "sdk-for-flutter-explore-core-threading-taskhandle-class"
---

<HTMLBlock>
<div class="sdk-for-flutter">
<!-- TaskHandle-class.html -->
<div class="doc-with-sidebar"><div class="sidebar-nav"><ol>
<li class="section-title"><a href="core.threading/TaskHandle-class.html#constructors">Constructors</a></li>
<li><a href="core.threading/TaskHandle/TaskHandle.html">TaskHandle</a></li>
<li class="section-title">
<a href="core.threading/TaskHandle-class.html#instance-properties">Properties</a>
</li>
<li class="inherited"><a href="core.threading/TaskHandle/hashCode.html">hashCode</a></li>
<li><a href="core.threading/TaskHandle/isCancelled.html">isCancelled</a></li>
<li><a href="core.threading/TaskHandle/isFinished.html">isFinished</a></li>
<li class="inherited"><a href="core.threading/TaskHandle/runtimeType.html">runtimeType</a></li>
<li class="section-title"><a href="core.threading/TaskHandle-class.html#instance-methods">Methods</a></li>
<li><a href="core.threading/TaskHandle/cancel.html">cancel</a></li>
<li class="inherited"><a href="core.threading/TaskHandle/noSuchMethod.html">noSuchMethod</a></li>
<li class="inherited"><a href="core.threading/TaskHandle/toString.html">toString</a></li>
<li class="section-title inherited"><a href="core.threading/TaskHandle-class.html#operators">Operators</a></li>
<li class="inherited"><a href="core.threading/TaskHandle/operator_equals.html">operator ==</a></li>
</ol></div><div class="doc-content">
<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li><a href="../index.html">/sdk-for-flutter-explore</a></li>
<li><a href="../core.threading/core.threading-library.html">/sdk-for-flutter-explore-core-threading-core-threading-library</a></li>
<li class="self-crumb">TaskHandle class</li>
</ol>
<div class="self-name">TaskHandle</div>
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
<div class="main-content" data-above-sidebar="core.threading/core.threading-library-sidebar.html" data-below-sidebar="core.threading/TaskHandle-class-sidebar.html" id="dartdoc-main-content">
<div>
<h1>TaskHandle class abstract</h1></div>
<section class="desc markdown">
<p>Handle used for the manipulation of the task.</p>
</section>
<section class="summary offset-anchor" id="constructors">
<h2>Constructors</h2>
<dl class="constructor-summary-list">
<dt class="callable" id="TaskHandle">
<a href="../core.threading/TaskHandle/TaskHandle.html">/sdk-for-flutter-explore-core-threading-taskhandle-taskhandle</a>(bool cancelLambda(), bool isFinishedGetLambda(), bool isCancelledGetLambda())
</dt>
<dd>
          Handle used for the manipulation of the task.
            <div class="constructor-modifier features">factory</div>
</dd>
</dl>
</section>
<section class="summary offset-anchor" id="instance-properties">
<h2>Properties</h2>
<dl class="properties">
<dt class="property inherited" id="hashCode">
<a href="../core.threading/TaskHandle/hashCode.html">/sdk-for-flutter-explore-core-threading-taskhandle-hashcode</a>
→ int
</dt>
<dd class="inherited">
  The hash code for this object.
  <div class="features">no setterinherited</div>
</dd>
<dt class="property" id="isCancelled">
<a href="../core.threading/TaskHandle/isCancelled.html">/sdk-for-flutter-explore-core-threading-taskhandle-iscancelled</a>
→ bool
</dt>
<dd>
  Completion indication.
True, if this task was canceled before it completed normally.
Gets a boolean indicating if this task is cancelled.
  <div class="features">no setter</div>
</dd>
<dt class="property" id="isFinished">
<a href="../core.threading/TaskHandle/isFinished.html">/sdk-for-flutter-explore-core-threading-taskhandle-isfinished</a>
→ bool
</dt>
<dd>
  Completion indication.
True, if this task is completed. Completion may be due to normal termination,
an exception, or cancellation - in all of these cases, result will return <code>true</code>.
Gets a boolean indicating if this task is completed.
  <div class="features">no setter</div>
</dd>
<dt class="property inherited" id="runtimeType">
<a href="../core.threading/TaskHandle/runtimeType.html">/sdk-for-flutter-explore-core-threading-taskhandle-runtimetype</a>
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
<dt class="callable" id="cancel">
<a href="../core.threading/TaskHandle/cancel.html">/sdk-for-flutter-explore-core-threading-taskhandle-cancel</a>(<wbr/>)
    → bool

</dt>
<dd>
  Sets internal state of task to 'canceled'.
  

</dd>
<dt class="callable inherited" id="noSuchMethod">
<a href="../core.threading/TaskHandle/noSuchMethod.html">/sdk-for-flutter-explore-core-threading-taskhandle-nosuchmethod</a>(<wbr/>Invocation invocation)
    → dynamic

</dt>
<dd class="inherited">
  Invoked when a nonexistent method or property is accessed.
  <div class="features">inherited</div>
</dd>
<dt class="callable inherited" id="toString">
<a href="../core.threading/TaskHandle/toString.html">/sdk-for-flutter-explore-core-threading-taskhandle-tostring</a>(<wbr/>)
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
<a href="../core.threading/TaskHandle/operator_equals.html">/sdk-for-flutter-explore-core-threading-taskhandle-operator-equals</a>(<wbr/>Object other)
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
<li><a href="../index.html">/sdk-for-flutter-explore</a></li>
<li><a href="../core.threading/core.threading-library.html">/sdk-for-flutter-explore-core-threading-core-threading-library</a></li>
<li class="self-crumb">TaskHandle class</li>
</ol>
<h5>core.threading library</h5>
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
