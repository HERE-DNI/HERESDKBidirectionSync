---
title: "PlatformThreading Protocol Reference"
slug: "sdk-for-ios-explore-protocols-platformthreading"
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

      runOnMainThread(runnable: )

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
  func runOnMainThread ( runnable : Runnable ) -> TaskHandle
  ```

  </pre>

  </div>

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

      postToMainThread(runnable: delayMs: )

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
  func postToMainThread ( runnable : Runnable , delayMs : UInt64 ) -> TaskHandle
  ```

  </pre>

  </div>

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

      postToMainThread(runnable: )

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
  func postToMainThread ( runnable : Runnable ) -> TaskHandle
  ```

  </pre>

  </div>

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

<div id="sdk-for-ios-explore-footer" class="section">

© 2026 . All rights reserved. (Last updated: 2026-04-14)

Generated by <a href="https://github.com/realm/jazzy" class="link" rel="external noopener" target="_blank">jazzy ♪♫ v0.15.2</a>, a <a href="https://realm.io" class="link" rel="external noopener" target="_blank">Realm</a> project.

</div>

</article>

