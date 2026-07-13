---
title: "PrefetchStatusListener class - prefetcher library - Dart API"
slug: "sdk-for-flutter-navigate-prefetcher-prefetchstatuslistener-class"
---

<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="prefetcher/prefetcher-library-sidebar.html" data-below-sidebar="prefetcher/PrefetchStatusListener-class-sidebar.html">

<div>

# <span class="kind-class">PrefetchStatusListener</span> class <a href="https://dart.dev/language/class-modifiers#abstract" class="feature feature-abstract" title="This type can not be directly constructed.">abstract</a>

</div>

<div class="section desc markdown">

Abstract class to get notified on status updates when prefetching map data.

</div>

## Constructors

<span class="name"><a href="sdk-for-flutter-navigate-prefetcher-prefetchstatuslistener-prefetchstatuslistener">PrefetchStatusListener</a></span><span class="signature">(<span id="sdk-for-flutter-navigate-param-onProgressLambda" class="parameter"><span class="type-annotation">void</span> <span class="parameter-name">onProgressLambda</span>(<span id="sdk-for-flutter-navigate-param" class="parameter"><span class="type-annotation">int</span></span>), </span><span id="sdk-for-flutter-navigate-param-onCompleteLambda" class="parameter"><span class="type-annotation">void</span> <span class="parameter-name">onCompleteLambda</span>(<span id="sdk-for-flutter-navigate-param" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-maploader-maploadererror">MapLoaderError</a>?</span></span>)</span>)</span>  
Abstract class to get notified on status updates when prefetching map data.

<div class="constructor-modifier features">

factory

</div>

## Properties

<span class="name"><a href="sdk-for-flutter-navigate-prefetcher-prefetchstatuslistener-hashcode">hashCode</a></span> <span class="signature">→ int</span>  
The hash code for this object.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-prefetcher-prefetchstatuslistener-runtimetype">runtimeType</a></span> <span class="signature">→ Type</span>  
A representation of the runtime type of the object.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

## Methods

<span class="name"><a href="sdk-for-flutter-navigate-prefetcher-prefetchstatuslistener-nosuchmethod">noSuchMethod</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-noSuchMethod-param-invocation" class="parameter"><span class="type-annotation">Invocation</span> <span class="parameter-name">invocation</span></span>) <span class="returntype parameter">→ dynamic</span> </span>  
Invoked when a nonexistent method or property is accessed.

<div class="features">

<span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-prefetcher-prefetchstatuslistener-oncomplete">onComplete</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-onComplete-param-error" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-maploader-maploadererror">MapLoaderError</a>?</span> <span class="parameter-name">error</span></span>) <span class="returntype parameter">→ void</span> </span>  
Called after the geo-corridor data downloads has been completed either with success or with error.

<span class="name"><a href="sdk-for-flutter-navigate-prefetcher-prefetchstatuslistener-onprogress">onProgress</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-onProgress-param-percentage" class="parameter"><span class="type-annotation">int</span> <span class="parameter-name">percentage</span></span>) <span class="returntype parameter">→ void</span> </span>  
Called multiple times to indicate the update progress.

<span class="name"><a href="sdk-for-flutter-navigate-prefetcher-prefetchstatuslistener-tostring">toString</a></span><span class="signature">(<wbr></wbr>) <span class="returntype parameter">→ String</span> </span>  
A string representation of this object.

<div class="features">

<span class="feature">inherited</span>

</div>

## Operators

<span class="name"><a href="sdk-for-flutter-navigate-prefetcher-prefetchstatuslistener-operator_equals">operator ==</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-param-other" class="parameter"><span class="type-annotation">Object</span> <span class="parameter-name">other</span></span>) <span class="returntype parameter">→ bool</span> </span>  
The equality operator.

<div class="features">

<span class="feature">inherited</span>

</div>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

