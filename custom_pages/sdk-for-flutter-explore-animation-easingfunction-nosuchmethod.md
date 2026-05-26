---
title: "noSuchMethod method"
slug: "sdk-for-flutter-explore-animation-easingfunction-nosuchmethod"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- noSuchMethod.html -->
<div class="doc-with-sidebar"><div class="doc-content">
<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li>/sdk-for-flutter-explore</li>
<li>/sdk-for-flutter-explore-animation-animation-library</li>
<li>/sdk-for-flutter-explore-animation-easingfunction</li>
<li class="self-crumb">noSuchMethod method</li>
</ol>
<div class="self-name">noSuchMethod</div>
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
<div class="main-content" data-above-sidebar="animation/EasingFunction-enum-sidebar.html" data-below-sidebar="" id="dartdoc-main-content">
<div>
<h1>noSuchMethod method</h1></div>
<section class="multi-line-signature">
dynamic
noSuchMethod(<wbr/><ol class="parameter-list single-line"> <li>Invocation invocation</li>
</ol>)

      <div class="features">inherited</div>
</section>
<section class="desc markdown">
<p>Invoked when a nonexistent method or property is accessed.</p>
<p>A dynamic member invocation can attempt to call a member which
doesn't exist on the receiving object. Example:</p>
<pre class="language-dart"><code class="language-dart">dynamic object = 1;
object.add(42); // Statically allowed, run-time error
</code></pre>
<p>This invalid code will invoke the <code>noSuchMethod</code> method
of the integer <code>1</code> with an <code>Invocation</code> representing the
<code>.add(42)</code> call and arguments (which then throws).</p>
<p>Classes can override <code>noSuchMethod</code> to provide custom behavior
for such invalid dynamic invocations.</p>
<p>A class with a non-default <code>noSuchMethod</code> invocation can also
omit implementations for members of its interface.
Example:</p>
<pre class="language-dart"><code class="language-dart">class MockList&lt;T&gt; implements List&lt;T&gt; {
  noSuchMethod(Invocation invocation) {
    log(invocation);
    super.noSuchMethod(invocation); // Will throw.
  }
}
void main() {
  MockList().add(42);
}
</code></pre>
<p>This code has no compile-time warnings or errors even though
the <code>MockList</code> class has no concrete implementation of
any of the <code>List</code> interface methods.
Calls to <code>List</code> methods are forwarded to <code>noSuchMethod</code>,
so this code will <code>log</code> an invocation similar to
<code>Invocation.method(#add, [42])</code> and then throw.</p>
<p>If a value is returned from <code>noSuchMethod</code>,
it becomes the result of the original invocation.
If the value is not of a type that can be returned by the original
invocation, a type error occurs at the invocation.</p>
<p>The default behavior is to throw a <code>NoSuchMethodError</code>.</p>
</section>
<section class="summary source-code" id="source">
<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">@pragma("vm:entry-point")
@pragma("wasm:entry-point")
external dynamic noSuchMethod(Invocation invocation);</code></pre>
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
<li>/sdk-for-flutter-explore-animation-animation-library</li>
<li>/sdk-for-flutter-explore-animation-easingfunction</li>
<li class="self-crumb">noSuchMethod method</li>
</ol>
<h5>EasingFunction enum</h5>
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
