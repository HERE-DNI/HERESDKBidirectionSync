---
title: "destroyLockingProcess method - LockingProcess class - core.engine library - Dart API"
slug: "sdk-for-flutter-explore-core-engine-lockingprocess-destroylockingprocess"
---

<div id="sdk-for-flutter-explore-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-explore-dartdoc-main-content" class="main-content" data-above-sidebar="core.engine/LockingProcess-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-method">destroyLockingProcess</span> static method

</div>

<div class="section multi-line-signature">

<span class="returntype">void</span> <span class="name">destroyLockingProcess</span>(<wbr></wbr>

1.  <span id="sdk-for-flutter-explore-destroyLockingProcess-param-sdkOptions" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-core-engine-sdkoptions-class">SDKOptions</a></span> <span class="parameter-name">sdkOptions</span>, </span>
2.  <span id="sdk-for-flutter-explore-destroyLockingProcess-param-maxTimeoutInMilliseconds" class="parameter"><span class="type-annotation">int</span> <span class="parameter-name">maxTimeoutInMilliseconds</span></span>

)

</div>

<div class="section desc markdown">

Checks if cache folder is locked.

Does nothing if cache is not locked or locked by current process. If cache is locked by a different process then the HERE SDK makes a few attempts to kill the locking application during the specified timeout. If it fails to kill the application, it attempts to remove the cache at <a href="sdk-for-flutter-explore-core-engine-sdkoptions-cachepath">SDKOptions.cachePath</a>. This function can be used before creating a SDKNativeEngine, i.e.

``` dart
final options = SDKOptions(...);
LockingProcess.destroyLockingProcess(options, 300);
final engine = SDKNativeEngine(options);
```

</pre>

- `sdkOptions` The options which are supposed to be used for a new instance of the engine.

- `maxTimeoutInMilliseconds` The maximum timeout in milliseconds. Recommended value is 300 - 500 milliseconds. If 0 or a negative value is passed then it makes only one attempt to kill the locking process (if any) and waits 30 milliseconds before exit because the system may spend a small amount of time to perform the operation.

</div>

## Implementation

``` dart
static void destroyLockingProcess(SDKOptions sdkOptions, int maxTimeoutInMilliseconds) => $prototype.destroyLockingProcess(sdkOptions, maxTimeoutInMilliseconds);
```

</pre>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

