---
title: "PlatformThreading Protocol Reference"
slug: "sdk-for-ios-navigate-protocols-platformthreading"
---

# PlatformThreading

<div class="declaration">

<div class="language">

``` highlight
public protocol PlatformThreading : AnyObject
```

</div>

</div>

Protocol for task activities on the main thread.

</div>

<div class="section section task-group-section">

<div class="task-group">

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk17PlatformThreadingP15runOnMainThread8runnableAA10TaskHandle_pAA8Runnable_p_tF"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Method-runOnMainThread-runnable" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-protocols-platformthreading#sdk-for-ios-navigate-s-7heresdk17PlatformThreadingP15runOnMainThread8runnableAA10TaskHandle_pAA8Runnable_p_tF" class="token"><code>runOnMainThread(runnable:</code><wbr></wbr><code>)</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Runs a task on the main thread. If this function is called from the main thread, then the task will run immediately. Otherwise, it is put to the end of the queue of the main thread. Note: Depending on actual platform, destruction-time of passed in runnable might be unknown due to unpredictability of garbage collection. Therefore, runnable should not hold strong references to objects whose lifetimes are critical or references should be released at the end of execution.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  func runOnMainThread(runnable: Runnable) -> TaskHandle
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-navigate-protocols-runnable">Runnable</a>
  - <a href="sdk-for-ios-navigate-protocols-taskhandle">TaskHandle</a>

  </div>

  <div>

  #### Parameters

  <table class="graybox">
  <colgroup>
  <col style="width: 50%" />
  <col style="width: 50%" />
  </colgroup>
  <tbody>
  <tr>
  <td><code> </code><em><code>runnable</code></em><code> </code></td>
  <td><div>
  <p>Task that should be executed on the main thread. Destruction-time of runnable is unknown.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  <div>

  #### Return Value

  Handle that will be used to manipulate execution of the task.

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk17PlatformThreadingP16postToMainThread8runnable7delayMsAA10TaskHandle_pAA8Runnable_p_s6UInt64VtF"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Method-postToMainThread-runnable-delayMs" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-protocols-platformthreading#sdk-for-ios-navigate-s-7heresdk17PlatformThreadingP16postToMainThread8runnable7delayMsAA10TaskHandle_pAA8Runnable_p_s6UInt64VtF" class="token"><code>postToMainThread(runnable:</code><wbr></wbr><code>delayMs:</code><wbr></wbr><code>)</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Posts a task to be executed on the main thread after some delay. If the delay is 0, the function puts the task at the end of the queue. The function does not wait for the task to be executed and returns immediately after the task has been put in the queue. Note: Depending on actual platform, destruction-time of passed in runnable might be unknown due to unpredictability of garbage collection. Therefore, runnable should not hold strong references to objects whose lifetimes are critical or references should be released at the end of execution.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  func postToMainThread(runnable: Runnable, delayMs: UInt64) -> TaskHandle
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-navigate-protocols-runnable">Runnable</a>
  - <a href="sdk-for-ios-navigate-protocols-taskhandle">TaskHandle</a>

  </div>

  <div>

  #### Parameters

  <table class="graybox">
  <colgroup>
  <col style="width: 50%" />
  <col style="width: 50%" />
  </colgroup>
  <tbody>
  <tr>
  <td><code> </code><em><code>runnable</code></em><code> </code></td>
  <td><div>
  <p>Task that should be executed on the main thread. Destruction-time of runnable is unknown.</p>
  </div></td>
  </tr>
  <tr>
  <td><code> </code><em><code>delayMs</code></em><code> </code></td>
  <td><div>
  <p>Delay in milliseconds.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  <div>

  #### Return Value

  Handle that will be used to manipulate execution of the task.

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk17PlatformThreadingP16postToMainThread8runnableAA10TaskHandle_pAA8Runnable_p_tF"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Method-postToMainThread-runnable" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-protocols-platformthreading#sdk-for-ios-navigate-s-7heresdk17PlatformThreadingP16postToMainThread8runnableAA10TaskHandle_pAA8Runnable_p_tF" class="token"><code>postToMainThread(runnable:</code><wbr></wbr><code>)</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Posts task to the end of the queue of the main thread. Function does not wait for task to be executed and returns immediately after the task is put to the queue. Note: Depending on actual platform, destruction-time of passed in runnable might be unknown due to unpredictability of garbage collection. Therefore, runnable should not hold strong references to objects whose lifetimes are critical or references should be released at the end of execution.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  func postToMainThread(runnable: Runnable) -> TaskHandle
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-navigate-protocols-runnable">Runnable</a>
  - <a href="sdk-for-ios-navigate-protocols-taskhandle">TaskHandle</a>

  </div>

  <div>

  #### Parameters

  <table class="graybox">
  <colgroup>
  <col style="width: 50%" />
  <col style="width: 50%" />
  </colgroup>
  <tbody>
  <tr>
  <td><code> </code><em><code>runnable</code></em><code> </code></td>
  <td><div>
  <p>Task that should be executed on the main thread. Destruction-time of runnable is unknown.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  <div>

  #### Return Value

  Handle that will be used to manipulate execution of the task.

  </div>

  </div>

  </div>

</div>

</div>

</div>

<div id="sdk-for-ios-navigate-footer" class="section">

© 2026 . All rights reserved. (Last updated: 2026-04-14)

Generated by <a href="https://github.com/realm/jazzy" class="link" rel="external noopener" target="_blank">jazzy ♪♫ v0.15.2</a>, a <a href="https://realm.io" class="link" rel="external noopener" target="_blank">Realm</a> project.

</div>

</article>

