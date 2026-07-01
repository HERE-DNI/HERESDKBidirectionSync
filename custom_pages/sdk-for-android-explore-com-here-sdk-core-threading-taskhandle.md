---
title: "TaskHandle (API Reference)"
slug: "sdk-for-android-explore-com-here-sdk-core-threading-taskhandle"
---

<div class="sub-title">

<span class="package-label-in-type">Package</span> [com.here.sdk.core.threading](sdk-for-android-explore-com-here-sdk-core-threading-package-summary)

</div>

<div id="class-description" class="section class-description">

<div class="type-signature">

<span class="modifiers">public interface
</span><span class="element-name type-name-label">TaskHandle</span>

</div>

<div class="block">

Handle used for the manipulation of the task.

</div>

</div>

<div class="section summary">

- <div id="method-summary" class="section method-summary">

  <div id="method-summary-table">

  <div class="table-tabs" aria-orientation="horizontal" role="tablist">

  All Methods
  Instance Methods
  Abstract Methods

  </div>

  <div id="method-summary-table.tabpanel"
  aria-labelledby="method-summary-table-tab0" role="tabpanel">

  <table>
  <colgroup>
  <col style="width: 33%" />
  <col style="width: 33%" />
  <col style="width: 33%" />
  </colgroup>
  <thead>
  <tr>
  <th>Modifier and Type</th>
  <th>Method</th>
  <th>Description</th>
  </tr>
  </thead>
  <tbody>
  <tr>
  <td><code>boolean</code></td>
  <td><pre><code>cancel()</code></pre></td>
  <td><div class="block">
  Sets internal state of task to 'canceled'.
  </div></td>
  </tr>
  <tr>
  <td><code>boolean</code></td>
  <td><pre><code>isCancelled()</code></pre></td>
  <td><div class="block">
  Gets a boolean indicating if this task is cancelled.
  </div></td>
  </tr>
  <tr>
  <td><code>boolean</code></td>
  <td><pre><code>isFinished()</code></pre></td>
  <td><div class="block">
  Gets a boolean indicating if this task is completed.
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  </div>

  </div>

</div>

<div class="section details">

- <div id="method-detail" class="section method-details">

  - <div id="cancel()" class="section detail">

    ### cancel

    <div class="member-signature">

    <span class="return-type">boolean</span> <span class="element-name">cancel</span>()

    </div>

    <div class="block">

    Sets internal state of task to 'canceled'. If the task is still in
    the queue, it will be removed from it immediately. However, if the
    task is in a running state, it will nevertheless be completed, as
    there is no way to interrupt it.

    </div>

    Returns:  
    True, if the task was canceled. False, if the task can't be canceled
    due to a platform dependent reason.

    </div>

  - <div id="isFinished()" class="section detail">

    ### isFinished

    <div class="member-signature">

    <span class="return-type">boolean</span> <span class="element-name">isFinished</span>()

    </div>

    <div class="block">

    Gets a boolean indicating if this task is completed. True, if this
    task is completed. Completion may be due to normal termination, an
    exception, or cancellation - in all of these cases, result will
    return true .

    </div>

    Returns:  
    Completion indication.

    </div>

  - <div id="isCancelled()" class="section detail">

    ### isCancelled

    <div class="member-signature">

    <span class="return-type">boolean</span> <span class="element-name">isCancelled</span>()

    </div>

    <div class="block">

    Gets a boolean indicating if this task is cancelled. True, if this
    task was canceled before it completed normally.

    </div>

    Returns:  
    Completion indication.

    </div>

  </div>

</div>

