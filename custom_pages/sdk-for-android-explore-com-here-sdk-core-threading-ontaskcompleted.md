---
title: "OnTaskCompleted (API Reference)"
slug: "sdk-for-android-explore-com-here-sdk-core-threading-ontaskcompleted"
---

<div class="sub-title">

<span class="package-label-in-type">Package</span> [com.here.sdk.core.threading](sdk-for-android-explore-com-here-sdk-core-threading-package-summary)

</div>

<div id="class-description" class="section class-description">

Functional Interface:  
This is a functional interface and can therefore be used as the
assignment target for a lambda expression or method reference.

<div class="type-signature">

<span class="annotations"><a
href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/FunctionalInterface.html"
class="external-link"
title="class or interface in java.lang">@FunctionalInterface</a>
</span><span class="modifiers">public interface
</span><span class="element-name type-name-label">OnTaskCompleted</span>

</div>

<div class="block">

The method will be called on the main thread when a task call has been
completed.

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
  <td><code>void</code></td>
  <td><pre><code>onTaskCompleted(TaskOutcome taskOutcome)</code></pre></td>
  <td><div class="block">
  The method will be called on the main thread when a task call has been
  completed.
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

  - <div id="onTaskCompleted(com.here.sdk.core.threading.TaskOutcome)"
    class="section detail">

    ### onTaskCompleted

    <div class="member-signature">

    <span class="return-type">void</span> <span class="element-name">onTaskCompleted</span><span class="parameters">(@NonNull
    [TaskOutcome](sdk-for-android-explore-com-here-sdk-core-threading-taskoutcome "enum class in com.here.sdk.core.threading") taskOutcome)</span>

    </div>

    <div class="block">

    The method will be called on the main thread when a task call has
    been completed.

    </div>

    Parameters:  
    `taskOutcome` -

    The task outcome

    </div>

  </div>

</div>

