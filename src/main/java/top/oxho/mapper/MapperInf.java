package top.oxho.mapper;

import org.apache.ibatis.annotations.Mapper;
import org.springframework.beans.factory.annotation.Autowired;
import top.oxho.pojo.Book;

@Mapper
public interface MapperInf {
    Book findAllUser();



}
