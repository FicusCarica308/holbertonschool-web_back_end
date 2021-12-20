// Task(1): a function getListStudentIds that returns an array of ids from a list of object.

export default function getListStudentIds(objs) {
  if (objs instanceof Array === false) {
    return [];
  }
  return (objs.map((obj) => obj.id));
}
