---
title: "eventTextListener property"
slug: "sdk-for-flutter-navigate-navigation-navigatorinterface-eventtextlistener"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- eventTextListener.html -->
<div class="doc-with-sidebar"><div class="doc-content">
<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li>/sdk-for-flutter-navigate</li>
<li>/sdk-for-flutter-navigate-navigation-navigation-library</li>
<li>/sdk-for-flutter-navigate-navigation-navigatorinterface-class</li>
<li class="self-crumb">eventTextListener property</li>
</ol>
<div class="self-name">eventTextListener</div>
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
<div class="main-content" data-above-sidebar="navigation/NavigatorInterface-class-sidebar.html" data-below-sidebar="" id="dartdoc-main-content">
<div>
<h1>eventTextListener property</h1></div>
<section id="getter">
<section class="multi-line-signature">
/sdk-for-flutter-navigate-navigation-eventtextlistener-class?
eventTextListener
</section>
<section class="desc markdown">
<p>Object to receive text notifications when they are available.
Setting <code>null</code> value to the listener will unset the listener.
It returns <code>null</code> when no listener is set by an user.
<strong>Note:</strong> In order to receive the text notification emitted for the traffic merge warner,
when <code>TrafficMergeWarningOptions.enable_text_notification</code> has been enabled, the <code>sdk.navigation.EventTextListener</code> must be enabled as well.
Gets the listener that notifies when a text notification is available.</p>
</section>
<section class="summary source-code" id="source">
<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">EventTextListener? get eventTextListener;</code></pre>
</section>
</section>
<section id="setter">
<section class="multi-line-signature">
void
eventTextListener=(<wbr/>/sdk-for-flutter-navigate-navigation-eventtextlistener-class? value)
</section>
<section class="desc markdown">
<p>Object to receive text notifications when they are available.
Setting <code>null</code> value to the listener will unset the listener.
It returns <code>null</code> when no listener is set by an user.
<strong>Note:</strong> In order to receive the text notification emitted for the traffic merge warner,
when <code>TrafficMergeWarningOptions.enable_text_notification</code> has been enabled, the <code>sdk.navigation.EventTextListener</code> must be enabled as well.
Sets the listener that notifies when a text notification is available.</p>
</section>
<section class="summary source-code" id="source">
<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">set eventTextListener(EventTextListener? value);</code></pre>
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
<li>/sdk-for-flutter-navigate-navigation-navigation-library</li>
<li>/sdk-for-flutter-navigate-navigation-navigatorinterface-class</li>
<li class="self-crumb">eventTextListener property</li>
</ol>
<h5>NavigatorInterface class</h5>
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
