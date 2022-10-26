<html>
<body>
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
<style>
.btn {
  background-color: DodgerBlue;
  border: none;
  color: white;
  padding: 12px 16px;
  font-size: 16px;
  cursor: pointer;
}
</style>
<a href="/"><button class="btn"><i class="fa fa-home"></i>Home</button></a>
<h2>Shopping List - Task 1</h2>
<hr/>
<table>
% for item in shopping_list:
  <tr>
    <td>{{str(item['desc'])}}</td>
    <td><a href="/task1/edit/{{str(item['id'])}}">edit</a></td>
    <td><a href="/task1/delete/{{str(item['id'])}}">delete</a></td>
  </tr>
% end
</table>
<hr/>
<form action="/task1/add/" method="post">
  <p>Add new item: <input name="description"/></p>
  <p><button type="submit">Submit</button></p>
</form>
<
</body>
</html>