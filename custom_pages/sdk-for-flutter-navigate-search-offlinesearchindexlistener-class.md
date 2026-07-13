---
title: "OfflineSearchIndexListener class - search library - Dart API"
slug: "sdk-for-flutter-navigate-search-offlinesearchindexlistener-class"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- OfflineSearchIndexListener-class.html -->
<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="search/search-library-sidebar.html" data-below-sidebar="search/OfflineSearchIndexListener-class-sidebar.html">

<div>

# <span class="kind-class">OfflineSearchIndexListener</span> class <a href="https://dart.dev/language/class-modifiers#abstract" class="feature feature-abstract" title="This type can not be directly constructed.">abstract</a>

</div>

<div class="section desc markdown">

Abstract class to get updates about progress of creating persistent map index.

Note: This is a beta release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process.

</div>

## Constructors

<span class="name"><a href="sdk-for-flutter-navigate-search-offlinesearchindexlistener-offlinesearchindexlistener">OfflineSearchIndexListener</a></span><span class="signature">(<span id="sdk-for-flutter-navigate-param-onStartedLambda" class="parameter"><span class="type-annotation">void</span> <span class="parameter-name">onStartedLambda</span>(<span id="sdk-for-flutter-navigate-param" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-search-offlinesearchindexoperation">OfflineSearchIndexOperation</a></span></span>), </span><span id="sdk-for-flutter-navigate-param-onProgressLambda" class="parameter"><span class="type-annotation">void</span> <span class="parameter-name">onProgressLambda</span>(<span id="sdk-for-flutter-navigate-param" class="parameter"><span class="type-annotation">int</span></span>), </span><span id="sdk-for-flutter-navigate-param-onCompleteLambda" class="parameter"><span class="type-annotation">void</span> <span class="parameter-name">onCompleteLambda</span>(<span id="sdk-for-flutter-navigate-param" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-search-offlinesearchindexerror">OfflineSearchIndexError</a>?</span></span>)</span>)</span>  
Abstract class to get updates about progress of creating persistent map index.

<div class="constructor-modifier features">

factory

</div>

## Properties

<span class="name"><a href="sdk-for-flutter-navigate-search-offlinesearchindexlistener-hashcode">hashCode</a></span> <span class="signature">→ int</span>  
The hash code for this object.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-search-offlinesearchindexlistener-runtimetype">runtimeType</a></span> <span class="signature">→ Type</span>  
A representation of the runtime type of the object.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

## Methods

<span class="name"><a href="sdk-for-flutter-navigate-search-offlinesearchindexlistener-nosuchmethod">noSuchMethod</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-noSuchMethod-param-invocation" class="parameter"><span class="type-annotation">Invocation</span> <span class="parameter-name">invocation</span></span>) <span class="returntype parameter">→ dynamic</span> </span>  
Invoked when a nonexistent method or property is accessed.

<div class="features">

<span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-search-offlinesearchindexlistener-oncomplete">onComplete</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-onComplete-param-error" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-search-offlinesearchindexerror">OfflineSearchIndexError</a>?</span> <span class="parameter-name">error</span></span>) <span class="returntype parameter">→ void</span> </span>  
Called after index creation or deletion has been completed.

<span class="name"><a href="sdk-for-flutter-navigate-search-offlinesearchindexlistener-onprogress">onProgress</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-onProgress-param-percentage" class="parameter"><span class="type-annotation">int</span> <span class="parameter-name">percentage</span></span>) <span class="returntype parameter">→ void</span> </span>  
Called multiple times to indicate the progress of index creation or deletion.

<span class="name"><a href="sdk-for-flutter-navigate-search-offlinesearchindexlistener-onstarted">onStarted</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-onStarted-param-operation" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-search-offlinesearchindexoperation">OfflineSearchIndexOperation</a></span> <span class="parameter-name">operation</span></span>) <span class="returntype parameter">→ void</span> </span>  
Called each time that the indexing has started.

<span class="name"><a href="sdk-for-flutter-navigate-search-offlinesearchindexlistener-tostring">toString</a></span><span class="signature">(<wbr></wbr>) <span class="returntype parameter">→ String</span> </span>  
A string representation of this object.

<div class="features">

<span class="feature">inherited</span>

</div>

## Operators

<span class="name"><a href="sdk-for-flutter-navigate-search-offlinesearchindexlistener-operator_equals">operator ==</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-param-other" class="parameter"><span class="type-annotation">Object</span> <span class="parameter-name">other</span></span>) <span class="returntype parameter">→ bool</span> </span>  
The equality operator.

<div class="features">

<span class="feature">inherited</span>

</div>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

</div>
`
}</HTMLBlock>
